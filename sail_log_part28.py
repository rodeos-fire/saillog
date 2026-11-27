# === Stage 28: Серии по дням ===
# Project: SailLog
from collections import OrderedDict


def group_consecutive_days(logs):
    """Group sail logs into series of consecutive days.

    Args:
        logs: iterable of sail-log records, each exposing a ``date``
            key. The date may be a real date object or any value that
            supports ``date()`` and ``timedelta`` (e.g. a string).
            Order of input is preserved.

    Returns:
        A list of series. Each series is an ordered mapping whose keys
        are human-readable labels (``"Day 1"`` ... ``"Day N"``) and
        whose values are the log records belonging to that day.
    """
    series = []
    current = None

    for log in logs:
        date = log["date"]
        current_date = _as_date(date)
        if current is None:
            current = {"date": current_date, "records": []}
            series.append(current)
        else:
            gap = (current_date - _as_date(current["date"])).days
            if gap == 1:
                current["records"].append(log)
            else:
                series.append(current)
                current = {"date": current_date, "records": [log]}

    if current is not None:
        series.append(current)

    return series


def _as_date(value):
    if hasattr(value, "date"):
        return value.date()
    if hasattr(value, "isoformat"):
        return value
    return datetime.date.fromisoformat(value)


def series_labels(series):
    """Return list of labels for each series in ``series``."""
    return ["Day %d" % (i + 1) for i in range(len(series))]


def series_summary(series):
    """Return list of (label, record_count) tuples for ``series``."""
    return [(label, len(records)) for label, records in zip(series_labels(series), series)]
