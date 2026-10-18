# test_leap.py
from leap import is_leap


def test_2024_is_a_leap_year():
    assert is_leap(2024)


def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)
