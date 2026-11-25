# === Stage 22: Просмотр истории ===
# Project: SailLog
from datetime import date


class Voyage:
    def __init__(self, yacht, route, wind, day):
        self.yacht = yacht
        self.route = route
        self.wind = wind
        self.day = day

    def history_line(self):
        return (
            f"{self.day.isoformat()} | {self.yacht} | "
            f"{self.route} | {self.wind} kt"
        )


def render_voyage_history(voyage):
    return voyage.history_line()


if __name__ == "__main__":
    sample = Voyage(
        yacht="Zephyr",
        route="Baltic Loop",
        wind=12,
        day=date(2024, 6, 14),
    )
    print(render_voyage_history(sample))
