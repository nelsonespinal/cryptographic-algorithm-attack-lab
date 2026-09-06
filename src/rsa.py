from .math_utils import gcd, mod_inverse
from .primes import generate_prime


def generate_keys(bits=16):
    # Generate two distinct prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)

    while q == p:
        q = generate_prime(bits)

    # Calculate n
    n = p * q

    # Calculate Euler's totient
    phi = (p - 1) * (q - 1)

    # Choose public exponent
    e = 65537

    # Make sure e and phi are relatively prime
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not relatively prime")

    # Calculate private exponent
    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key, p, q, phi


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


def validate_message(message_number, public_key):
    _, n = public_key

    if message_number >= n:
        raise ValueError("Message is too large for this RSA key")

    if message_number < 0:
        raise ValueError("Message must be non-negative")


def text_to_number(text):
    return int.from_bytes(text.encode("utf-8"), "big")


def number_to_text(number):
    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, "big").decode("utf-8")

