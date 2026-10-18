# leap.py
def is_leap(year):
    """Return True if year is a leap year in the Gregorian calendar."""
    if year < 1:
        raise ValueError("year must be 1 or later")
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
