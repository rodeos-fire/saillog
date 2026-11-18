# === Stage 5: Удаление и восстановление ===
# Project: SailLog
"""Soft-delete support for the SailLog 'trip' entity."""

import uuid
from datetime import datetime


class Trip:
    def __init__(self, boat, route, wind, date):
        self.id = uuid.uuid4().hex
        self.boat = boat
        self.route = route
        self.wind = wind
        self.date = date
        self.deleted = False
        self.deleted_at = None

    def delete(self):
        self.deleted = True
        self.deleted_at = datetime.now()

    def restore(self):
        if self.deleted:
            self.deleted = False
            self.deleted_at = None
            return True
        return False


class SailLogStore:
    def __init__(self):
        self._trips = {}

    def add(self, boat, route, wind, date):
        trip = Trip(boat, route, wind, date)
        self._trips[trip.id] = trip
        return trip

    def soft_delete(self, trip_id):
        trip = self._trips.get(trip_id)
        if trip is None:
            return False
        trip.delete()
        return True

    def restore(self, trip_id):
        trip = self._trips.get(trip_id)
        if trip is None or not trip.deleted:
            return False
        trip.restore()
        return True

    def get(self, trip_id):
        return self._trips.get(trip_id)

    def list_active(self):
        return [t for t in self._trips.values() if not t.deleted]

    def list_deleted(self):
        return [t for t in self._trips.values() if t.deleted]
