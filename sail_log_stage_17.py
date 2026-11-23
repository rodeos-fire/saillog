# === Stage 17: Слияние записей ===
# Project: SailLog
def merge_sailings(sailings, field):
    """Return the winning value for a given field across two sailings.

    The winner is chosen by a fixed priority:
        1. longer distance wins
        2. faster average speed wins
        3. stronger wind wins
        4. earlier date wins
        5. the yacht name wins alphabetically (lexicographically smaller)
    """
    candidates = [s for s in sailings if s.get(field) is not None]
    if len(candidates) < 2:
        return None
    return max(candidates, key=lambda s: _score(s, field))


def _score(sailing, field):
    """Build a comparable score tuple for a single field.

    Each element is a (key, value) pair so that larger keys take priority,
    and larger values win within the same key.
    """
    value = sailing.get(field)
    if field == "distance":
        return (1, float(value) if value is not None else float("-inf"))
    if field == "average_speed":
        return (1, float(value) if value is not None else float("-inf"))
    if field == "wind_speed":
        return (1, float(value) if value is not None else float("-inf"))
    if field == "date":
        parsed = _parse_date(value)
        return (1, -parsed if parsed is not None else float("-inf"))
    return (0, value if value is not None else "")


def _parse_date(value):
    """Convert a date string into a sortable tuple.

    Accepts 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS' and returns a tuple
    that compares chronologically. Returns None for unparseable values.
    """
    try:
        if len(value) >= 10:
            return (int(value[0:4]), int(value[5:7]), int(value[8:10]))
        return (int(value[0:4]), int(value[5:7]), int(value[8:10]), 0, 0, 0)
    except (ValueError, TypeError):
        return None
