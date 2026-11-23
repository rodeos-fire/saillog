# === Stage 19: Статусы записей ===
# Project: SailLog
class SailOutStatus:
    PLANNED = "planned"
    ON_WATER = "on_water"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


_TRANSITIONS = {
    SailOutStatus.PLANNED: (SailOutStatus.ON_WATER, SailOutStatus.CANCELLED),
    SailOutStatus.ON_WATER: (SailOutStatus.COMPLETED, SailOutStatus.CANCELLED),
    SailOutStatus.COMPLETED: (),
    SailOutStatus.CANCELLED: (),
}


def can_transition(from_status, to_status):
    if from_status not in _TRANSITIONS:
        return False
    return to_status in _TRANSITIONS[from_status]


def allowed_transitions(status):
    return _TRANSITIONS.get(status, ())


def is_terminal(status):
    return status in (SailOutStatus.COMPLETED, SailOutStatus.CANCELLED)
