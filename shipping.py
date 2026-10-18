import math


def shipping_fee(weight_kg):
    """Return the shipping fee in baht for a parcel of weight_kg kilograms.

    Rule 1. The weight must be more than 0 kg. Otherwise raise ValueError.
    Rule 2. A parcel of up to 1 kg costs 40 baht.
    Rule 3. A parcel of more than 1 kg and up to 5 kg costs 60 baht.
    Rule 4. A parcel of more than 5 kg costs 60 baht plus 10 baht for every
    started kilogram above 5 kg. A 5.2 kg parcel costs 70 baht.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be more than 0 kg")
    if weight_kg <= 1:
        return 40
    if weight_kg <= 5:
        return 60
    extra = math.ceil(weight_kg - 5)
    return 60 + 10 * extra
