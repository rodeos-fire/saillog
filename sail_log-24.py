# === Stage 24: Недельный отчёт ===
# Project: SailLog
from datetime import date


class WeeklyReport:
    """Builds a textual weekly report from sailings and beats."""

    def __init__(self, sailings, beats_by_sailing):
        self.sailings = sailings
        self.beats_by_sailing = beats_by_sailing

    def _sailings_in_week(self, week_start):
        result = []
        for sailing in self.sailings:
            d = sailing.date
            if week_start <= d < week_start + _SEVEN_DAYS:
                result.append(sailing)
        return result

    def _beats_for_sailing(self, sailing):
        return self.beats_by_sailing.get(id(sailing), [])

    def _wind_summary(self, sailings):
        if not sailings:
            return "none"
        winds = []
        for sailing in sailings:
            if sailing.wind:
                winds.append(sailing.wind)
        return ", ".join(sorted(set(winds))) if winds else "none"

    def _route_summary(self, sailings):
        if not sailings:
            return "none"
        routes = []
        for sailing in sailings:
            if sailing.route:
                routes.append(sailing.route)
        return "; ".join(sorted(set(routes))) if routes else "none"

    def _build_table(self, week_start, sailings):
        lines = []
        lines.append("Week of %s" % week_start)
        lines.append("=" * 60)
        lines.append("")
        lines.append("Sailing      Route          Wind        "
                     "Sailings   Beats")
        lines.append("-" * 60)
        for sailing in sailings:
            beats = self._beats_for_sailing(sailing)
            lines.append("%-15s %-14s %-9s %4d   %d"
                         % (sailing.yacht, sailing.route or "-",
                            sailing.wind or "-", len(sailings), len(beats)))
        lines.append("")
        if sailings:
            lines.append("Distinct winds: %s" % self._wind_summary(sailings))
            lines.append("Distinct routes: %s" % self._route_summary(sailings))
        else:
            lines.append("No sailings this week.")
        return "\n".join(lines)

    def report_for_week(self, week_start):
        sailings = self._sailings_in_week(week_start)
        return self._build_table(week_start, sailings)


_SEVEN_DAYS = date.resolution * 7
