# === Stage 29: Средняя скорость ===
# Project: SailLog
from datetime import datetime

__all__ = ["SegmentSpeed", "average_segment_speed"]


class SegmentSpeed:
    """Average speed over a single leg of a sailing route.

    Speed is computed as the distance covered divided by the elapsed
    time, expressed in knots (nautical miles per hour).
    """

    def __init__(self, distance_nm, start_time, end_time):
        self.distance_nm = float(distance_nm)
        self._start = self._parse(start_time)
        self._end = self._parse(end_time)

    @staticmethod
    def _parse(value):
        if not isinstance(value, datetime):
            raise TypeError("time must be a datetime object")
        return value

    @property
    def duration_hours(self):
        return (self._end - self._start).total_seconds() / 3600.0

    @property
    def speed_knots(self):
        if self.duration_hours <= 0:
            return 0.0
        return self.distance_nm / self.duration_hours

    def __repr__(self):
        return (
            f"SegmentSpeed(distance_nm={self.distance_nm}, "
            f"speed_knots={self.speed_knots:.2f})"
        )


def average_segment_speed(segments):
    """Return the mean speed across an iterable of SegmentSpeed objects.

    Segments with non-positive duration are skipped so they do not
    skew the average. Returns 0.0 when no valid segments remain.
    """
    valid = [s for s in segments if s.duration_hours > 0]
    if not valid:
        return 0.0
    total = sum(s.speed_knots for s in valid)
    return total / len(valid)
