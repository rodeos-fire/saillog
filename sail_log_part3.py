# === Stage 3: Хранилище в памяти ===
# Project: SailLog
from typing import Dict, List, Optional

__all__ = ["SailTrip", "InMemoryTripStore"]


class SailTrip:
    """An in-sail exit: a yacht on a route under a wind on a given date."""

    def __init__(self, trip_id: str, yacht: str, route: str,
                 wind: str, date: str):
        self.trip_id = trip_id
        self.yacht = yacht
        self.route = route
        self.wind = wind
        self.date = date

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SailTrip):
            return NotImplemented
        return self.trip_id == other.trip_id and \
            self.yacht == other.yacht and \
            self.route == other.route and \
            self.wind == other.wind and \
            self.date == other.date

    def __repr__(self) -> str:
        return (f"SailTrip(id={self.trip_id!r}, yacht={self.yacht!r}, "
                f"route={self.route!r}, wind={self.wind!r}, "
                f"date={self.date!r})")


class InMemoryTripStore:
    """A tiny in-memory store for SailTrip records keyed by trip id."""

    def __init__(self) -> None:
        self._records: Dict[str, SailTrip] = {}

    def add(self, trip: SailTrip) -> SailTrip:
        """Insert or replace a trip record and return it."""
        self._records[trip.trip_id] = trip
        return trip

    def get(self, trip_id: str) -> Optional[SailTrip]:
        """Return the trip with the given id or None when absent."""
        return self._records.get(trip_id)

    def list(self) -> List[SailTrip]:
        """Return all stored trips as an independent list."""
        return list(self._records.values())

    def __len__(self) -> int:
        return len(self._records)
