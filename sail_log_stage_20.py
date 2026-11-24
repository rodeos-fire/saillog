# === Stage 20: Смена статуса ===
# Project: SailLog
from enum import Enum


class SailLogStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ABANDONED = "abandoned"


class SailLogTransitionError(Exception):
    pass


class SailLogReason:
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def __str__(self):
        return f"{self.status}: {self.message}"


_TRANSITIONS = {
    SailLogStatus.SCHEDULED: {
        SailLogStatus.IN_PROGRESS: "sailed",
        SailLogStatus.ABANDONED: "abandoned before start",
    },
    SailLogStatus.IN_PROGRESS: {
        SailLogStatus.COMPLETED: "finished",
        SailLogStatus.ABANDONED: "called off",
    },
    SailLogStatus.SCHEDULED: {
        SailLogStatus.COMPLETED: "ran without sailing",
    },
}


def change_sail_log_status(sail_log, new_status, reason):
    if new_status not in SailLogStatus:
        raise SailLogTransitionError(f"unknown status: {new_status}")

    if sail_log.status == new_status:
        raise SailLogTransitionError("new status equals current status")

    valid_reason = None
    if new_status in SailLogStatus.IN_PROGRESS:
        valid_reason = "start"
    elif new_status in SailLogStatus.COMPLETED:
        valid_reason = "finish"
    elif new_status in SailLogStatus.ABANDONED:
        valid_reason = "cancel"

    if reason is None:
        reason = SailLogReason(new_status, valid_reason or "no reason")
    else:
        if not isinstance(reason, SailLogReason):
            reason = SailLogReason(new_status, str(reason))
        if reason.status != new_status:
            raise SailLogTransitionError("reason does not match new status")

    sail_log.status = new_status
    sail_log.reason = reason
    return sail_log
