"""
Шифр "Виженера"
"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            keyword_char = keyword[i % len(keyword)]
            plain_char = plaintext[i]
            if plaintext[i].islower():
                ascii_value = 97
            else:
                ascii_value = 65
            key_shift = ord(keyword_char) - ascii_value
            char_shift = ord(plain_char) - ascii_value
            encrypted_shift = (key_shift + char_shift) % 26
            encrypted_char = chr(encrypted_shift + ascii_value)
            ciphertext += encrypted_char
        else:
            ciphertext += plaintext[i]

    return ciphertext


PLAINTEXT = input("Enter a word: ")
KEYWORD = input("Enter a keyword: ")
CIPHERTEXT = encrypt_vigenere(PLAINTEXT, KEYWORD)

print(f"Encrypted word: {CIPHERTEXT}")


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            keyword_char = keyword[i % len(keyword)]
            cipher_char = char
            if char.islower():
                ascii_value = 97
            else:
                ascii_value = 65
            key_shift = ord(keyword_char) - ascii_value
            char_shift = ord(cipher_char) - ascii_value
            shift = (char_shift - key_shift + 26) % 26

            decrypted_char = chr(shift + ascii_value)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


CIPHERTEXT = input("Enter cipher: ")
KEYWORD = input("Enter keyword: ")
PLAINTEXT = decrypt_vigenere(CIPHERTEXT, KEYWORD)

print(f"Decrypted word: {PLAINTEXT}")
