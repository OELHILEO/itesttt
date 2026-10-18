import pytest
from shipping import shipping_fee


# Rule 1: Weight must be > 0.
def test_rule_1_negative_weight_raises():
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(-1)


# Breaks Rule 1: weight of 0 kg must raise ValueError, but code allows 0 kg
def test_rule_1_zero_weight_raises():
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(0)


# Parametrized tests for valid fees according to Rules 2, 3, and 4
@pytest.mark.parametrize(
    "weight_kg, expected_fee",
    [
        # Rule 2: up to 1 kg costs 40 baht
        (0.5, 40),
        # Breaks Rule 2: exactly 1 kg should cost 40 baht, but code uses weight < 1 and returns 60
        (1.0, 40),
        # Rule 3: more than 1 kg and up to 5 kg costs 60 baht
        (1.1, 60),
        (3.0, 60),
        (5.0, 60),
        # Rule 4: more than 5 kg costs 60 + 10 for every started kg above 5 kg
        # Breaks Rule 4: 5.2 kg parcel costs 70 baht, but int(0.2) truncates to 0 giving 60
        (5.2, 70),
        (6.0, 70),
        (6.1, 80),
    ],
)
def test_shipping_fee(weight_kg, expected_fee):
    assert shipping_fee(weight_kg) == expected_fee
