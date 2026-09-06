from .frequency_analysis import english_score

def encrypt_caesar(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


def break_caesar(ciphertext):
    results = []

    for shift in range(26):
        plaintext = decrypt_caesar(ciphertext, shift)
        score = english_score(plaintext)

        results.append((score, shift, plaintext))

    results.sort()

    return results

