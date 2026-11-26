# === Stage 25: Месячный отчёт ===
# Project: SailLog
import calendar
from datetime import datetime


def format_month_header(year, month):
    name = calendar.month_name[month]
    return f"{name} {year}"


def format_wind_direction(value):
    value = str(value).strip().lower()
    if value in ("n", "north", "north wind", "north wind, light"):
        return "N"
    if value in ("s", "south", "south wind"):
        return "S"
    if value in ("e", "east", "east wind"):
        return "E"
    if value in ("w", "west", "west wind"):
        return "W"
    return value


def summarize_sailings(sailings):
    total_sailings = len(sailings)
    total_hours = 0
    total_distance = 0
    total_points = 0
    total_sailors = 0
    sailings_by_point_of_sail = {}
    sailings_by_wind = {}
    sailings_by_route = {}

    for sailing in sailings:
        legs = sailing.get("legs", [])
        for leg in legs:
            total_hours += leg.get("hours", 0)
            total_distance += leg.get("distance_nm", 0)
            point_of_sail = leg.get("point_of_sail")
            if point_of_sail:
                sailings_by_point_of_sail[point_of_sail] = \
                    sailings_by_point_of_sail.get(point_of_sail, 0) + 1
            wind = leg.get("wind")
            if wind:
                wind_key = (wind.get("direction"), wind.get("force_beaufort"))
                sailings_by_wind.setdefault(wind_key, []).append(wind)
        route = sailing.get("route")
        if route:
            sailings_by_route[route] = sailings_by_route.get(route, 0) + 1
        sailors = sailing.get("sailors", [])
        for sailor in sailors:
            total_sailors += 1

    summary = {
        "total_sailings": total_sailings,
        "total_hours": total_hours,
        "total_distance_nm": total_distance,
        "total_points": total_points,
        "total_sailors": total_sailors,
        "sailings_by_point_of_sail": sailings_by_point_of_sail,
        "sailings_by_wind": sailings_by_wind,
        "sailings_by_route": sailings_by_route,
    }
    return summary
