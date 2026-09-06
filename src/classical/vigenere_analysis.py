from collections import Counter
from .frequency_analysis import english_score


def index_of_coincidence(text):
    letters = [char.upper() for char in text if char.isalpha()]

    n = len(letters)

    if n < 2:
        return 0.0

    counts = Counter(letters)

    numerator = sum(
        count * (count - 1)
        for count in counts.values()
    )

    denominator = n * (n - 1)

    return numerator / denominator


def average_ic_for_key_length(text, key_length):
    letters = [char.upper() for char in text if char.isalpha()]

    columns = [
        letters[i::key_length]
        for i in range(key_length)
    ]

    ic_values = [
        index_of_coincidence(column)
        for column in columns
    ]

    return sum(ic_values) / len(ic_values)


def estimate_key_lengths(text, max_key_length=12):
    results = []

    for key_length in range(1, max_key_length + 1):
        avg_ic = average_ic_for_key_length(text, key_length)

        results.append((avg_ic, key_length))

    results.sort(reverse=True)

    return results


def recover_caesar_shift(column):
    best_score = float("inf")
    best_shift = 0

    for shift in range(26):
        decrypted = ""

        for char in column:
            shifted = (ord(char) - ord("A") - shift) % 26
            decrypted += chr(ord("A") + shifted)

        score = english_score(decrypted)

        if score < best_score:
            best_score = score
            best_shift = shift

    return best_shift


def recover_vigenere_key(text, key_length):
    letters = [char.upper() for char in text if char.isalpha()]

    key = ""

    for i in range(key_length):
        column = letters[i::key_length]

        shift = recover_caesar_shift(column)

        key += chr(ord("A") + shift)

    return key

