# === Stage 7: Связи между сущностями ===
# Project: SailLog
from datetime import datetime

class Sailboat:
    def __init__(self, name):
        self.name = name

class Route:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

class Wind:
    def __init__(self, direction, speed):
        self.direction = direction
        self.speed = speed

class SailingTrip:
    def __init__(self, boat, route, wind, date):
        self.boat = boat
        self.route = route
        self.wind = wind
        self.date = date
        self.galss = []

    def add_gals(self, gals):
        self.galss.extend(gals)

    def get_galss(self):
        if self.galss is None:
            raise ValueError("Gals list is not initialized for this trip")
        return list(self.gals)

    def validate_link(self, gals):
        if gals is None:
            raise ValueError("Gals list is empty or not provided")
        if len(gals) == 0:
            raise ValueError("No gals recorded for this sailing trip")
        for gals_item in gals:
            if not hasattr(gals_item, "trip"):
                raise TypeError("Each gals must have a 'trip' attribute")
            if gals_item.trip is not self:
                raise ValueError("Gals do not belong to the given sailing trip")

class Gals:
    def __init__(self, trip, role, position):
        self.trip = trip
        self.role = role
        self.position = position

def get_galss_for_trip(trip, gals):
    trip.validate_link(gals)
    return trip.get_galss()

if __name__ == "__main__":
    boat = Sailboat("Ocean")
    route = Route("Coast", "Point A", "Point B")
    wind = Wind("North", 15)
    trip = SailingTrip(boat, route, wind, datetime(2024, 5, 1))

    g1 = Gals(trip, "helm", "front")
    g2 = Gals(trip, "navigator", "middle")
    g3 = Gals(trip, "sailmaker", "back")
    all_gals = [g1, g2, g3]

    trip.add_gals(all_gals)
    result = get_galss_for_trip(trip, all_gals)
    for g in result:
        print(g.role, g.position)
