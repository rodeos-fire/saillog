# === Stage 6: Связанная сущность ===
# Project: SailLog
# sail_log_sail.py - SailLog: sailing log module for adding a "sail" (галс) entity
# A "sail" (галс) is a single leg of a voyage, linked to a "voyage" (выход)
# by the voyage identifier. This module is self-contained and uses only the
# Python standard library.

from datetime import datetime


# SailPoint is the unique identifier of a sail within a voyage.
class SailPoint:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return "SailPoint(%s)" % self.value

    def __eq__(self, other):
        return isinstance(other, SailPoint) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


# Sail is a sailing leg (галс) associated with a voyage (выход) via SailPoint.
class Sail:
    def __init__(self, voyage_point, start_time, wind, crew):
        self.voyage_point = SailPoint(voyage_point)
        self.start_time = datetime.fromisoformat(start_time)
        self.wind = wind
        self.crew = crew

    def __str__(self):
        return (
            "Sail(voyage=%s, start=%s, wind=%s, crew=%s)"
            % (self.voyage_point, self.start_time, self.wind, self.crew)
        )

    def __repr__(self):
        return str(self)


# add_sail creates a Sail entity and registers it into a voyage.
# voyage is a dictionary that stores a list of sails under the key "sails".
# The sail is linked to the voyage through the voyage identifier (voyage_point).
# Returns the created Sail instance.
def add_sail(voyage, voyage_point, start_time, wind, crew):
    sail = Sail(voyage_point, start_time, wind, crew)

    if "sails" not in voyage:
        voyage["sails"] = []

    voyage["sails"].append(sail)

    return sail
