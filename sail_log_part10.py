# === Stage 10: Сортировка записей ===
# Project: SailLog
from datetime import datetime


def sort_key(record):
    return (record["yacht"].lower(), record["created_at"])


def sort_expeditions(records, reverse=False):
    return sorted(records, key=sort_key, reverse=reverse)
