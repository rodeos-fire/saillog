# === Stage 4: Редактирование записей ===
# Project: SailLog
import datetime

VALID_YACHTS = {"SeaBreeze", "NorthernStar", "BlueHorizon"}
VALID_ROUTES = {"coastal", "offshore", "cruising"}
VALID_WINDS = {"light", "moderate", "strong", "gale"}

EDITABLE_FIELDS = {"yacht", "route", "wind"}


def normalize_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    return None


def validate_sailout(data):
    if not isinstance(data, dict):
        return False
    for field in EDITABLE_FIELDS:
        if field not in data:
            return False
        value = data[field]
        if field == "yacht":
            if value not in VALID_YACHTS:
                return False
        elif field == "route":
            if value not in VALID_ROUTES:
                return False
        elif field == "wind":
            if value not in VALID_WINDS:
                return False
    return True


def apply_edit(sailout, field, value):
    if field not in EDITABLE_FIELDS:
        raise ValueError(f"Field '{field}' is not editable")
    if field == "yacht":
        if value not in VALID_YACHTS:
            raise ValueError(f"Invalid yacht: {value}")
        sailout["yacht"] = value
    elif field == "route":
        if value not in VALID_ROUTES:
            raise ValueError(f"Invalid route: {value}")
        sailout["route"] = value
    elif field == "wind":
        if value not in VALID_WINDS:
            raise ValueError(f"Invalid wind: {value}")
        sailout["wind"] = value
    return True


def edit_sailout_by_id(sailouts, sailout_id, field, value):
    for sailout in sailouts:
        if sailout["id"] == sailout_id:
            apply_edit(sailout, field, value)
            return True
    return False
