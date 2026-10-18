# Test list:
# ☑ 200 g × 3 = 600 g
# ☑ multiplying a quantity does not modify the original
# ☑ two quantities with the same amount and unit are equal
# ☑ 1 oz is not the same as 1 g
# ☐ 200 g + 300 g = 500 g
# ☐ 200 g + 1 oz, reduced to grams, using a conversion rate
# ☐ (200 g + 1 oz) × 2

from kitchen import Quantity, grams, ounces


def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)
