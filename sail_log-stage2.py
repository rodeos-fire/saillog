# === Stage 2: Проверка полей ===
# Project: SailLog
import datetime


def normalize_yacht(value):
    """Normalize yacht identifier: strip whitespace and uppercase."""
    if value is None:
        return ""
    return str(value).strip().upper()


def normalize_route(value):
    """Normalize route: strip whitespace."""
    if value is None:
        return ""
    return str(value).strip()


def normalize_wind(value):
    """Normalize wind direction: strip whitespace and uppercase."""
    if value is None:
        return ""
    return str(value).strip().upper()


def normalize_date(value):
    """Normalize date into a datetime.date object."""
    if value is None:
        return None
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {value!r}")


def validate_sail_out(sail_out):
    """Validate a sail-out record and return a list of error messages.

    Each field must be present; invalid values are reported with
    human-readable messages. Returns an empty list when the record is
    valid.
    """
    errors = []

    yacht = normalize_yacht(sail_out.get("yacht"))
    if not yacht:
        errors.append("Yacht identifier is required.")

    route = normalize_route(sail_out.get("route"))
    if not route:
        errors.append("Route is required.")

    wind = normalize_wind(sail_out.get("wind"))
    if not wind:
        errors.append("Wind is required.")

    date = normalize_date(sail_out.get("date"))
    if date is None:
        errors.append("A valid date is required.")

    return errors


def build_sail_out(raw, yachts=None):
    """Build and validate a sail-out record.

    Accepts a raw dictionary from user input. Returns a normalized
    dictionary on success or a tuple (None, [errors]) on failure.
    """
    errors = validate_sail_out(raw)
    if errors:
        return None, errors

    return {
        "yacht": normalize_yacht(raw.get("yacht")),
        "route": normalize_route(raw.get("route")),
        "wind": normalize_wind(raw.get("wind")),
        "date": normalize_date(raw.get("date")),
    }, []
