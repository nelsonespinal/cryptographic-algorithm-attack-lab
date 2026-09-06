from src.classical.vigenere import encrypt_vigenere
from src.classical.vigenere_analysis import (
    index_of_coincidence,
    estimate_key_lengths,
    recover_vigenere_key,
)

def test_index_of_coincidence_repeated_letters():
    ic = index_of_coincidence("AAAAAAAAAA")

    assert ic == 1.0


def test_index_of_coincidence_short_text():
    assert index_of_coincidence("A") == 0.0


def test_estimate_key_length():
    plaintext = (
        "THIS IS A LONG ENGLISH MESSAGE THAT CONTAINS ENOUGH TEXT "
        "TO MAKE FREQUENCY BASED CRYPTANALYSIS MORE RELIABLE. "
        "WE ARE USING THIS MESSAGE TO TEST WHETHER THE PROGRAM "
        "CAN IDENTIFY THE LENGTH OF A VIGENERE CIPHER KEY. "
    ) * 5

    key = "LEMON"

    ciphertext = encrypt_vigenere(plaintext, key)

    results = estimate_key_lengths(ciphertext, max_key_length=10)

    top_lengths = [
        key_length
        for _, key_length in results[:3]
    ]

    assert len(key) in top_lengths


def test_recover_vigenere_key():
    plaintext = (
        "THIS IS A LONG ENGLISH MESSAGE THAT CONTAINS ENOUGH TEXT "
        "TO MAKE FREQUENCY BASED CRYPTANALYSIS MORE RELIABLE. "
        "WE ARE USING THIS MESSAGE TO TEST WHETHER THE PROGRAM "
        "CAN RECOVER THE SECRET VIGENERE KEY USING FREQUENCY ANALYSIS. "
    ) * 10

    key = "LEMON"

    ciphertext = encrypt_vigenere(plaintext, key)

    recovered_key = recover_vigenere_key(
        ciphertext,
        len(key)
    )

    assert recovered_key == key