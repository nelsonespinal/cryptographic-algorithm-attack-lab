from src.math_utils import gcd, extended_gcd, mod_inverse

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(17, 5) == 1
    assert gcd(270, 192) == 6


def test_extended_gcd():
    gcd_value, x, y = extended_gcd(48, 18)

    assert gcd_value == 6
    assert 48 * x + 18 * y == gcd_value


def test_mod_inverse():
    assert mod_inverse(3, 7) == 5
    assert mod_inverse(10, 17) == 12