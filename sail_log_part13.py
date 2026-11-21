# === Stage 13: Группировка ===
# Project: SailLog
from collections import OrderedDict


def group_by_route(sailings):
    groups = OrderedDict()
    for sailing in sailings:
        route = sailing["route"]
        groups[route] = groups.get(route, 0) + 1
    return groups


def group_by_route_verbose(sailings):
    groups = OrderedDict()
    for sailing in sailings:
        route = sailing["route"]
        entry = groups.get(route)
        if entry is None:
            entry = []
            groups[route] = entry
        entry.append(sailing)
    return groups


def count_by_route(sailings):
    counts = {}
    for sailing in sailings:
        route = sailing["route"]
        counts[route] = counts.get(route, 0) + 1
    return counts


def top_routes(sailings, limit=5):
    tally = count_by_route(sailings)
    ordered = sorted(tally.items(), key=lambda item: item[1], reverse=True)
    return ordered[:limit]


def render_summary(sailings):
    tally = count_by_route(sailings)
    total = sum(tally.values())
    lines = ["Sailings by route:"]
    for route, count in sorted(tally.items()):
        lines.append("  {:<20} {}".format(route, count))
    lines.append("  {:<20} {}".format("TOTAL", total))
    return "\n".join(lines)


def group_and_count(sailings, key="route"):
    result = []
    for sailing in sailings:
        result.append((sailing[key], 1))
    tally = OrderedDict()
    for route, increment in result:
        tally[route] = tally.get(route, 0) + increment
    return tally


def group_and_count_verbose(sailings, key="route"):
    groups = OrderedDict()
    for sailing in sailings:
        route = sailing[key]
        entry = groups.get(route)
        if entry is None:
            entry = []
            groups[route] = entry
        entry.append(sailing)
    return groups


def group_and_count_sailings(sailings, key="route"):
    groups = OrderedDict()
    for sailing in sailings:
        route = sailing[key]
        entry = groups.get(route)
        if entry is None:
            entry = []
            groups[route] = entry
        entry.append(sailing)
    return groups


def group_and_count_verbose_sailings(sailings, key="route"):
    tally = OrderedDict()
    for sailing in sailings:
        route = sailing[key]
        tally[route] = tally.get(route, 0) + 1
    return tally


def group_and_count_verbose_counts(sailings, key="route"):
    counts = OrderedDict()
    for sailing in sailings:
        route = sailing[key]
        counts[route] = counts.get(route, 0) + 1
    return counts


def group_and_count_verbose_totals(sailings, key="route"):
    counts = OrderedDict()
    for sailing in sailings:
        route = sailing[key]
