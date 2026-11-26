# === Stage 26: Скользящее среднее ===
# Project: SailLog
from collections import deque


def moving_average(values, window):
    """Return a list of rolling averages over the given numeric sequence.

    Each output element is the mean of up to ``window`` consecutive input
    values, so the first element covers only the first value when the
    sequence is shorter than ``window``.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")
    if not values:
        return []

    window = max(window, 1)
    buffer = deque(values, maxlen=window)
    result = []
    for total, _ in zip(
        _accumulate(buffer), range(1, len(values) + 1)
    ):
        result.append(total / len(buffer))
    return result


def _accumulate(iterable):
    """Yield running sums like :func:`itertools.accumulate` without importing it.

    Kept local so the module stays self-contained while reusing a simple
    generator to pair each sum with its position.
    """
    total = 0
    for index, value in enumerate(iterable):
        total += value
        yield total, index


def average_wind_speed(galley_averages):
    """Compute the overall average of per-galley wind speeds.

    ``galley_averages`` is a sequence of numbers, one per gybe. Returns the
    mean value rounded to two decimals, or 0.0 when there is nothing to
    average.
    """
    if not galley_averages:
        return 0.0
    return round(sum(galley_averages) / len(galley_averages), 2)


def trend_direction(values):
    """Describe whether a numeric series is rising, falling or stable.

    Compares the last two values and returns one of ``"up"``, ``"down"``
    or ``"stable"``. Returns ``"none"`` for a sequence with fewer than two
    elements.
    """
    if len(values) < 2:
        return "none"
    previous, current = values[-2], values[-1]
    if current > previous:
        return "up"
    if current < previous:
        return "down"
    return "stable"


def summarize_sail_out(sail_out, window=5):
    """Build a small summary report for a single sail out.

    ``sail_out`` must expose a ``wind_indicator`` numeric field. The result
    is a dictionary with the rolling average of that indicator over the last
    ``window`` recorded values plus the detected trend.
    """
    series = deque(
        sail_out.wind_indicator, maxlen=window
    ) if hasattr(sail_out, "wind_indicator") else list(sail_out)
    return {
        "moving_average": moving_average(series, window),
        "trend": trend_direction(series),
    }
