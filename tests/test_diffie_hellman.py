from src.diffie_hellman import (
    generate_private_key,
    generate_public_key,
    generate_shared_secret,
)


def test_shared_secret_matches():
    p = 23
    g = 5

    alice_private = generate_private_key(p)
    bob_private = generate_private_key(p)

    alice_public = generate_public_key(g, alice_private, p)
    bob_public = generate_public_key(g, bob_private, p)

    alice_secret = generate_shared_secret(
        bob_public,
        alice_private,
        p
    )

    bob_secret = generate_shared_secret(
        alice_public,
        bob_private,
        p
    )

    assert alice_secret == bob_secret