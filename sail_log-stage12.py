# === Stage 12: Теги ===
# Project: SailLog
from typing import List, Dict, Optional, Tuple


class SailLogTag:
    """Represents a tag attached to an outing record."""

    def __init__(self, name: str, color: str = "default"):
        self.name = name
        self.color = color

    def __eq__(self, other: object) -> bool:
        return isinstance(other, SailLogTag) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"Tag({self.name!r}, {self.color!r})"


def add_tag(outing: Dict, tag: SailLogTag) -> None:
    """Add a tag to the outing's tag list."""
    if "tags" not in outing:
        outing["tags"] = set()
    outing["tags"].add(tag)


def remove_tag(outing: Dict, tag: SailLogTag) -> bool:
    """Remove a tag from the outing. Returns True if a tag was removed."""
    if not outing.get("tags"):
        return False
    return outing["tags"].discard(tag)


def search_by_tag(outings: List[Dict], tag: SailLogTag) -> List[Dict]:
    """Return all outings that carry the given tag."""
    return [o for o in outings if tag in o.get("tags", set())]


def has_tag(outing: Dict, tag: SailLogTag) -> bool:
    """Check if the outing contains the given tag."""
    return tag in outing.get("tags", set())
