# === Stage 27: Аномальные значения ===
# Project: SailLog
from statistics import mean, pstdev


def detect_outliers(sailings, threshold_std=3.0):
    """Return list of sailings whose numeric field is a statistical outlier."""
    numeric_fields = ("wind_speed", "distance", "duration", "crew_count", "course_length")
    field_values = {field: [s.get(field, 0) for s in sailings] for field in numeric_fields}
    outliers = [s for s in sailings for field in numeric_fields if is_anomaly(s, field, field_values)]
    return outliers


def is_anomaly(sailing, field, field_values):
    values = field_values[field]
    if len(values) < 3:
        return False
    average = mean(values)
    spread = pstdev(values)
    if spread == 0:
        return False
    return abs(sailing.get(field, 0) - average) > threshold_std * spread
