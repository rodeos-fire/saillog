# === Stage 8: Генерация идентификаторов ===
# Project: SailLog
from collections import defaultdict
from datetime import datetime


PROJECT_PREFIX = "SL"

IDENTITY_COUNTERS = defaultdict(int)


def generate_id(prefix, table, value, suffix=""):
    candidate = f"{prefix}_{value}{suffix}"
    if not any(
        id_ in IDENTITY_COUNTERS
        and IDENTITY_COUNTERS[id_] > 0
        and candidate in IDENTITY_COUNTERS
        for id_, count in IDENTITY_COUNTERS.items()
    ):
        IDENTITY_COUNTERS[candidate] = 0
        return candidate
    counter = IDENTITY_COUNTERS[candidate]
    while True:
        collision = False
        for id_, count in IDENTITY_COUNTERS.items():
            if count > 0 and candidate == id_:
                collision = True
                break
        if not collision:
            IDENTITY_COUNTERS[candidate] = counter
            return candidate
        counter += 1


def clear_id_counters():
    IDENTITY_COUNTERS.clear()
