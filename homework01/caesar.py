"""
Шифр "Цезарь"
"""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ascii_value = 97
            else:
                ascii_value = 65
            encrypted_char = chr(
                (ord(char) - ascii_value + shift) % 26 + ascii_value
            )  # noqa
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


TEXT = input("Enter a word: ")
SHIFT_NUMBER = int(input("Enter a shift: "))
encrypted_word = encrypt_caesar(TEXT, SHIFT_NUMBER)
print("Encrypted word:", encrypted_word)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                ascii_value = 97
            else:
                ascii_value = 65
            decrypted_word = chr(
                (ord(char) - ascii_value - shift) % 26 + ascii_value
            )  # noqa
            plaintext += decrypted_word
        else:
            plaintext += char
    return plaintext


CIPHERTEXT = input("Enter cipher: ")
SHIFT_NUMBER = int(input("Enter shift: "))

decrypted_char = decrypt_caesar(CIPHERTEXT, SHIFT_NUMBER)
print("Decrypted word:", decrypted_char)
