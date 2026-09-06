from src.classical.caesar import encrypt_caesar, decrypt_caesar


def test_caesar_encryption():
    assert encrypt_caesar("HELLO", 3) == "KHOOR"


def test_caesar_decryption():
    assert decrypt_caesar("KHOOR", 3) == "HELLO"