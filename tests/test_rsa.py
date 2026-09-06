from src.rsa import(
    generate_keys,
    encrypt,
    decrypt,
    text_to_number,
    number_to_text,
)


def test_rsa_encryption():
    public_key, private_key, _, _, _ = generate_keys(bits = 32)

    message = 42

    ciphertext = encrypt(message, public_key)
    decrypted = decrypt(ciphertext, private_key)

    assert decrypted == message


def test_rsa_text_encryption():
    public_key, private_key, _, _, _ = generate_keys(bits = 32)

    message = "HELLO"

    message_number = text_to_number(message)
    ciphertext = encrypt(message_number, public_key)
    decrypted_number = decrypt(ciphertext, private_key)
    decrypted_message = number_to_text(decrypted_number)

    assert decrypted_message == message

