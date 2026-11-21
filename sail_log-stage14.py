# === Stage 14: Постраничный вывод ===
# Project: SailLog
"""SailLog pagination module: page number and page size for the sail-out list."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Page:
    """A single page of results for the sail-out list."""

    page: int
    size: int
    items: List[dict] = field(default_factory=list)
    total: int = 0
    total_pages: int = 0

    def is_empty(self) -> bool:
        return not self.items

    def has_next(self) -> bool:
        return self.page < self.total_pages

    def has_prev(self) -> bool:
        return self.page > 1


@dataclass
class PagedRequest:
    """Query parameters for paging the sail-out list."""

    page: int = 1
    size: int = 10

    def validate(self) -> "PagedRequest":
        if self.page < 1:
            self.page = 1
        if self.size < 1:
            self.size = 1
        return self


def paginate(items: List[dict], page: int, size: int) -> Page:
    """Slice a list of sail-outs into a single page."""

    request = PagedRequest(page, size).validate()
    start = (request.page - 1) * request.size
    end = start + request.size
    return Page(
        page=request.page,
        size=request.size,
        items=items[start:end],
        total=len(items),
        total_pages=(len(items) + request.size - 1) // request.size,
    )


def build_query_string(page: int, size: int) -> str:
    """Render pagination controls as a simple query string."""

    request = PagedRequest(page, size).validate()
    return f"?page={request.page}&size={request.size}"
