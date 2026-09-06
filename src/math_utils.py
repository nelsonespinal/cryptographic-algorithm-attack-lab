def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


def mod_inverse(a, m):
    gcd_value, x, y = extended_gcd(a, m)

    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist")

    return x % m

