from src.classical.vigenere import (
    encrypt_vigenere,
    decrypt_vigenere,
)


def test_vigenere_encryption():
    assert encrypt_vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"


def test_vigenere_decryption():
    assert decrypt_vigenere("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"

