import hashlib

def hash_message(message):
    digest = hashlib.sha256(message.encode("utf-8")).digest()
    return int.from_bytes(digest, "big")


def sign_message(message, private_key):
    d, n = private_key

    message_hash = hash_message(message)

    if message_hash >= n:
        message_hash %= n

    signature = pow(message_hash, d, n)

    return signature


def verify_signature(message, signature, public_key):
    e, n = public_key

    expected_hash = hash_message(message)

    if expected_hash >= n:
        expected_hash %= n

    recovered_hash = pow(signature, e, n)

    return recovered_hash == expected_hash

