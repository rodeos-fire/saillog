# === Stage 9: Фильтрация записей ===
# Project: SailLog
from datetime import datetime


def filter_sailouts(sailouts, route=None, start_date=None, end_date=None):
    start_dt = _to_date(start_date)
    end_dt = _to_date(end_date)
    filtered = []
    for sailout in sailouts:
        if route is not None and sailout.get("route") != route:
            continue
        if start_dt is not None and sailout["date"] < start_dt:
            continue
        if end_dt is not None and sailout["date"] > end_dt:
            continue
        filtered.append(sailout)
    return filtered


def _to_date(value):
    if value is None:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def filter_by_route(sailouts, route):
    return filter_sailouts(sailouts, route=route)


def filter_by_date_range(sailouts, start_date, end_date):
    return filter_sailouts(sailouts, start_date=start_date, end_date=end_date)


def filter_by_route_and_date(sailouts, route, start_date, end_date):
    return filter_sailouts(
        sailouts, route=route, start_date=start_date, end_date=end_date
    )


if __name__ == "__main__":
    sample = [
        {"yacht": "Dufour 42", "route": "Cape", "wind": 12, "date": "2024-05-01"},
        {"yacht": "J/Boats 32", "route": "Fjord", "wind": 8, "date": "2024-06-15"},
        {"yacht": "Dufour 42", "route": "Cape", "wind": 20, "date": "2024-07-20"},
    ]
    print(filter_by_route(sample, "Cape"))
    print(filter_by_date_range(sample, "2024-06-01", "2024-07-31"))
    print(filter_by_route_and_date(sample, "Cape", "2024-06-01", "2024-07-31"))
