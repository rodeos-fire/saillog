# === Stage 23: Общая сводка ===
# Project: SailLog
from collections import Counter

SAILING_DATE_FORMAT = "%Y-%m-%d"


def sailing_date(value):
    return datetime.strptime(value, SAILING_DATE_FORMAT).date()


def sailing_summary(joyhs):
    if not joyhs:
        return {
            "count": 0,
            "routes": {},
            "latest": [],
        }

    by_route = Counter(joyh["route"] for joyh in joyhs)
    latest = sorted(joyhs, key=sailing_date, reverse=True)[:5]

    return {
        "count": len(joyhs),
        "routes": dict(sorted(by_route.items(), key=lambda item: item[1], reverse=True)),
        "latest": latest,
    }
