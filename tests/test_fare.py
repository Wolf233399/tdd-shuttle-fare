import pytest
from fare import fare_cents, weekly_total


def test_short_trip_adult_pays_base_fare():
    # Arrange
    distance_km = 3
    # Act
    result = fare_cents(distance_km, "adult")
    # Assert
    assert result == 200


def test_exactly_five_km_adult_pays_base_fare():
    assert fare_cents(5, "adult") == 200


def test_eight_km_adult_costs_350():
    assert fare_cents(8, "adult") == 350


def test_eight_km_student_pays_half():
    assert fare_cents(8, "student") == 175


def test_child_rides_free():
    assert fare_cents(20, "child") == 0


def test_negative_distance_is_an_error():
    with pytest.raises(ValueError):
        fare_cents(-1, "adult")


def test_unknown_rider_is_an_error():
    with pytest.raises(ValueError):
        fare_cents(3, "pilot")


def test_part_of_a_km_is_charged_as_a_full_km():
    assert fare_cents(5.5, "adult") == 250


def test_peak_hours_add_100_cent_surcharge():
    assert fare_cents(3, "adult", peak=True) == 300


def test_student_pays_half_of_the_peak_surcharge_too():
    assert fare_cents(3, "student", peak=True) == 150


@pytest.mark.parametrize("distance_km, rider, expected", [
    (0, "adult", 200),
    (5, "adult", 200),
    (5.1, "adult", 250),
    (6, "adult", 250),
    (10, "student", 225),
    (10, "senior", 225),
    (100, "child", 0),
    (4.9, "adult", 200),
    (5.01, "adult", 250),
    (20, "senior", 475),

])
def test_fare_table(distance_km, rider, expected):
    assert fare_cents(distance_km, rider) == expected

def test_weekly_total_of_no_trips_is_zero():
    assert weekly_total([]) == 0


def test_weekly_total_under_the_cap_is_the_sum():
    assert weekly_total([200, 200, 200]) == 600


def test_weekly_total_exactly_at_the_cap():
    assert weekly_total([500, 500, 500]) == 1500


def test_weekly_total_never_goes_over_the_cap():
    assert weekly_total([500, 500, 500, 500]) == 1500


def test_weekly_total_rejects_a_negative_fare():
    with pytest.raises(ValueError):
        weekly_total([200, -50])

