from math import isqrt

from ..math_utils import mod_inverse


def factor_modulus(n):
    """
    Factor an RSA modulus n = p * q using trial division.

    This is intentionally designed for small educational RSA keys.
    """

    if n % 2 == 0:
        return 2, n // 2

    limit = isqrt(n)

    for factor in range(3, limit + 1, 2):
        if n % factor == 0:
            return factor, n // factor

    raise ValueError("Could not factor modulus")


def recover_private_key(public_key):
    e, n = public_key

    p, q = factor_modulus(n)

    phi = (p - 1) * (q - 1)

    d = mod_inverse(e, phi)

    return d, n

