from src.attacks.rsa_factorization import (
    factor_modulus,
    recover_private_key,
)

from src.rsa import (
    generate_keys,
    encrypt,
    decrypt,
)


def test_factor_modulus():
    p = 61
    q = 53

    n = p * q

    recovered_p, recovered_q = factor_modulus(n)

    assert recovered_p * recovered_q == n


def test_recover_private_key():
    public_key, private_key, _, _, _ = generate_keys(bits=8)

    recovered_private_key = recover_private_key(public_key)

    assert recovered_private_key == private_key


def test_rsa_factorization_attack():
    public_key, _, _, _, _ = generate_keys(bits=8)

    message = 42

    ciphertext = encrypt(message, public_key)

    # Attacker reconstructs the private key
    recovered_private_key = recover_private_key(public_key)

    # Attacker decrypts the ciphertext
    recovered_message = decrypt(
        ciphertext,
        recovered_private_key
    )

    assert recovered_message == message

    