import math

BASE_FARE_CENTS = 200
INCLUDED_KM = 5
PER_EXTRA_KM_CENTS = 50
DISCOUNTS = {"adult": 1.0, "student": 0.5, "senior": 0.5, "child": 0.0}


def fare_cents(distance_km, rider="adult"):
    """Return the shuttle fare in cents.

    Rules (the specification):
      - The base fare of 200 cents covers the first 5 km (including exactly 5 km).
      - Each additional km, or part of a km, costs 50 cents.
      - Students and seniors pay half. Children ride free.
      - A negative distance or an unknown rider type raises ValueError.
    """
    if distance_km < 0:
        raise ValueError("distance must be non-negative")
    if rider not in DISCOUNTS:
        raise ValueError(f"unknown rider type: {rider}")
    extra_km = max(0, math.ceil(distance_km - INCLUDED_KM))
    full = BASE_FARE_CENTS + extra_km * PER_EXTRA_KM_CENTS
    return int(full * DISCOUNTS[rider])
