from src.primes import is_prime, generate_prime

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(97) is True

    assert is_prime(1) is False
    assert is_prime(100) is False
    assert is_prime(221) is False


def test_generate_prime():
    prime = generate_prime(16)

    assert is_prime(prime) is True
    assert prime.bit_length() == 16

