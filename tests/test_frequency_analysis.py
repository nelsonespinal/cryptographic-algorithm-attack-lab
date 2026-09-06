from src.classical.caesar import encrypt_caesar, break_caesar


def test_break_caesar():
    plaintext = (
        "THIS IS A LONGER ENGLISH MESSAGE USED TO TEST "
        "FREQUENCY ANALYSIS FOR A CAESAR CIPHER"
    )

    ciphertext = encrypt_caesar(plaintext, 3)

    results = break_caesar(ciphertext)

    best_score, best_shift, best_plaintext = results[0]

    assert best_shift == 3
    assert best_plaintext == plaintext

