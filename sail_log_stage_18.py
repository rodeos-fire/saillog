# === Stage 18: Избранное ===
# Project: SailLog
from typing import List, Dict, Optional

FAVORITE_FIELDS = ("marked", "marked_at")


def mark_favorite(log: Dict, sail_id: str, mark: bool) -> None:
    """Toggle the favorite flag on a single sail entry.

    Args:
        log: Mutable dict keyed by ``"sails"`` containing the sail records.
        sail_id: Identifier of the sail to update.
        mark: When truthy the flag is set and a timestamp is recorded;
              when falsy the flag is cleared.

    Raises:
        KeyError: If ``sail_id`` is not present in the log.
        ValueError: If toggling off is requested for an entry that was never
            marked as favorite.
    """
    if sail_id not in log["sails"]:
        raise KeyError(f"Sail {sail_id!r} not found in log.")

    sail = log["sails"][sail_id]
    if mark:
        sail["marked"] = True
        sail["marked_at"] = _now_iso()
    else:
        if not sail.get("marked"):
            raise ValueError(
                f"Sail {sail_id!r} is not marked as favorite; cannot unmark."
            )
        sail["marked"] = False
        sail.pop("marked_at", None)


def _now_iso() -> str:
    """Return the current local time formatted as an ISO 8601 string."""
    import datetime

    return datetime.datetime.now().isoformat(timespec="seconds")


def list_favorites(log: Dict) -> List[str]:
    """Return the identifiers of all sails currently marked as favorite.

    The result is ordered by the ``marked_at`` timestamp so the most recent
    selections appear first. Entries lacking a timestamp are ignored, which
    keeps the function robust against partially initialised records.
    """
    entries = [
        sail for sail in log["sails"].values() if sail.get("marked")
    ]
    entries.sort(key=lambda s: s.get("marked_at", ""), reverse=True)
    return [sail["id"] for sail in entries]


def clear_favorite(log: Dict, sail_id: str) -> bool:
    """Remove the favorite flag from a sail and return whether it changed.

    Returns:
        ``True`` if the sail was marked and got unmarked, ``False``
        otherwise. Never raises for a missing flag; callers that need
        strict behaviour should verify membership separately.
    """
    sail = log["sails"].get(sail_id)
    if sail is None:
        return False
    if sail.get("marked"):
        mark_favorite(log, sail_id, False)
        return True
    return False
