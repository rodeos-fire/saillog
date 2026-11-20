# === Stage 11: Поиск по нескольким словам ===
# Project: SailLog
"""SailLog: multi-key search with exclusion terms.

Finds sailings that match several required keywords while ignoring any
sailing that contains one of the exclusion keywords.  The search is case
insensitive and works on the sailing identifier, route, wind and date.
"""

from collections import defaultdict


class Sailing:
    """A single sailing made by a yacht."""

    def __init__(self, yacht, route, wind, date):
        self.yacht = yacht
        self.route = route
        self.wind = wind
        self.date = date

    def __repr__(self):
        return (
            "Sailing(yacht={!r}, route={!r}, wind={!r}, date={!r})".format(
                self.yacht, self.route, self.wind, self.date
            )
        )


def _iter_tokens(text):
    """Yield lowercase words from a string, skipping punctuation."""
    for word in text.lower().split():
        word = word.strip(".,;:!?")
        if word:
            yield word


def build_index(sailings):
    """Build a token -> set(sailing) index for fast lookups."""
    index = defaultdict(set)
    for sailing in sailings:
        for field in (sailing.yacht, sailing.route, sailing.wind, sailing.date):
            for token in _iter_tokens(field):
                index[token].add(sailing)
    return index


def search(sailings, terms):
    """Return sailings matching *all* terms and none of the exclusions.

    *terms* is a list of strings.  A leading dash marks an exclusion
    keyword, for example ``["Baltic", "Finn", "-Storm"]``.
    """
    if not terms:
        return list(sailings)

    index = build_index(sailings)
    required = []
    excluded = []
    for term in terms:
        if term.startswith("-"):
            excluded.append(term[1:].strip().lower())
        else:
            required.append(term.strip().lower())

    if not required:
        return [s for s in sailings if not any(
            s in index[token] for token in excluded
        )]

    # Start from the smallest required bucket to keep the work minimal.
    buckets = [index[token] for token in required]
    if not buckets:
        return []
    candidates = min(buckets, key=len)

    result = []
    exclude_set = set(excluded)
    for sailing in candidates:
        if sailing in exclude_set:
            continue
        match = True
        for token in required:
            if sailing not in index[token]:
                match = False
                break
        if match:
            result.append(sailing)
    return result
