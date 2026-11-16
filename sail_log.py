# === Stage 1: Каркас модуля ===
# Project: SailLog
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class SailingTrip:
    """A single sailing trip (exit) recorded in the log."""
    yacht: str
    route: str
    wind: str
    date: date
    legs: List["Leg"] = field(default_factory=list)
    crew: List[str] = field(default_factory=list)
