def encrypt_vigenere(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")

            shift = ord(key[key_index % len(key)]) - ord("A")

            encrypted_char = chr(
                (ord(char) - base + shift) % 26 + base
            )

            result += encrypted_char
            key_index += 1
        else:
            result += char

    return result


def decrypt_vigenere(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")

            shift = ord(key[key_index % len(key)]) - ord("A")

            decrypted_char = chr(
                (ord(char) - base - shift) % 26 + base
            )

            result += decrypted_char
            key_index += 1
        else:
            result += char

    return result

