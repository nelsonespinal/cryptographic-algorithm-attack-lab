import random

# step 4
def is_prime(n, rounds=10):
    if n < 2:
        return False

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if n in small_primes:
        return True

    for prime in small_primes:
        if n % prime == 0:
            return False

    # Write n - 1 as d * 2^s
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    # Miller-Rabin rounds
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:
            return False

    return True

def generate_prime(bits=16):
    while True:
        candidate = random.getrandbits(bits)

        # Make sure the number has the requested bit length
        candidate |= (1 << (bits - 1))

        # Make sure the number is odd
        candidate |= 1

        if is_prime(candidate):
            return candidate

