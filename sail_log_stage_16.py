# === Stage 16: Поиск дубликатов ===
# Project: SailLog
from datetime import datetime

def _normalize_wind(wind_str):
    if not wind_str:
        return None
    return wind_str.strip().lower()

def _normalize_route(route_str):
    if not route_str:
        return None
    return route_str.strip().lower()

def _normalize_yacht(yacht_str):
    if not yacht_str:
        return None
    return yacht_str.strip().lower()

def _normalize_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").isoformat()
    except (ValueError, TypeError):
        return None

def _signature(sail_out):
    return (
        _normalize_yacht(sail_out.get("yacht")),
        _normalize_route(sail_out.get("route")),
        _normalize_wind(sail_out.get("wind")),
        _normalize_date(sail_out.get("date")),
    )

def find_duplicate_sail_outs(sail_outs):
    if not sail_outs:
        return []
    seen = {}
    duplicates = []
    for sail_out in sail_outs:
        key = _signature(sail_out)
        if key in seen:
            duplicates.append(sail_out)
        else:
            seen[key] = sail_out
    return duplicates

def remove_duplicate_sail_outs(sail_outs):
    if not sail_outs:
        return []
    seen = set()
    unique = []
    for sail_out in sail_outs:
        key = _signature(sail_out)
        if key not in seen:
            seen.add(key)
            unique.append(sail_out)
    return unique
