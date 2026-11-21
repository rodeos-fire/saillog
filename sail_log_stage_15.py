# === Stage 15: Быстрые фильтры ===
# Project: SailLog
from datetime import date, timedelta


def _parse_date(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def is_today(sail_date):
    parsed = _parse_date(sail_date)
    return parsed is not None and parsed == date.today()


def is_this_week(sail_date, week_anchors=None):
    parsed = _parse_date(sail_date)
    if parsed is None:
        return False
    if week_anchors is None:
        week_anchors = _default_week_anchors(date.today())
    start, end = week_anchors
    return start <= parsed <= end


def is_overdue(sail_date, reference=None):
    parsed = _parse_date(sail_date)
    if parsed is None:
        return False
    if reference is None:
        reference = date.today()
    return parsed < reference


def _default_week_anchors(reference):
    start_of_week = reference - timedelta(days=reference.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def build_date_filters(reference=None, week_anchors=None):
    if reference is None:
        reference = date.today()
    if week_anchors is None:
        week_anchors = _default_week_anchors(reference)
    return {
        "today": is_today,
        "this_week": partial(_this_week_bound, week_anchors),
        "overdue": partial(_overdue_bound, reference),
    }


def partial(func, *args, **kwargs):
    def wrapper(*call_args, **call_kwargs):
        return func(*args, *call_args, **kwargs, **call_kwargs)
    return wrapper


def _this_week_bound(sail_date, week_anchors):
    return is_this_week(sail_date, week_anchors)


def _overdue_bound(sail_date, reference):
    return is_overdue(sail_date, reference)


def classify_sail_date(sail_date, reference=None, week_anchors=None):
    filters = build_date_filters(reference, week_anchors)
    buckets = {"today": [], "this_week": [], "overdue": []}
    if sail_date is None:
        return buckets.get("none", [])
    for key, predicate in filters.items():
        if predicate(sail_date):
            buckets[key].append(sail_date)
    return buckets
