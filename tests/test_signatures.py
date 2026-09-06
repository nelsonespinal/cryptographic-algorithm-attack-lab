from src.rsa import generate_keys
from src.signatures import sign_message, verify_signature

def test_valid_signature():
    public_key, private_key, _, _, _ = generate_keys(bits=32)

    message = "HELLO"

    signature = sign_message(message, private_key)

    assert verify_signature(message, signature, public_key) is True


def test_modified_message_fails():
    public_key, private_key, _, _, _ = generate_keys(bits=32)

    message = "HELLO"

    signature = sign_message(message, private_key)

    assert verify_signature("HELLo", signature, public_key) is False