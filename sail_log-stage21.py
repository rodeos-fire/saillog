# === Stage 21: История изменений ===
# Project: SailLog
from datetime import datetime


class Change:
    def __init__(self, field, old_value, new_value, timestamp):
        self.field = field
        self.old_value = old_value
        self.new_value = new_value
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f"Change(field={self.field!r}, "
            f"old={self.old_value!r}, "
            f"new={self.new_value!r}, "
            f"at={self.timestamp!r})"
        )


class SailingTrip:
    def __init__(self, yacht, route, wind, date):
        self.yacht = yacht
        self.route = route
        self.wind = wind
        self.date = date
        self.changes = []

    def _log(self, field, old_value, new_value):
        self.changes.append(
            Change(field, old_value, new_value, datetime.now())
        )

    def set_yacht(self, yacht):
        self._log("yacht", self.yacht, yacht)
        self.yacht = yacht

    def set_route(self, route):
        self._log("route", self.route, route)
        self.route = route

    def set_wind(self, wind):
        self._log("wind", self.wind, wind)
        self.wind = wind

    def set_date(self, date):
        self._log("date", self.date, date)
        self.date = date

    def as_dict(self):
        return {
            "yacht": self.yacht,
            "route": self.route,
            "wind": self.wind,
            "date": self.date,
            "changes": [
                {
                    "field": c.field,
                    "old_value": c.old_value,
                    "new_value": c.new_value,
                    "timestamp": c.timestamp.isoformat(),
                }
                for c in self.changes
            ],
        }
