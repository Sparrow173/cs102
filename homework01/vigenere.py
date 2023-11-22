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
    for i, char in enumerate(plaintext):
        if char.isalpha():
            keyword_char = keyword[i % len(keyword)]
            if char.islower():
                ascii_value = ord('a')
            else:
                ascii_value = ord('A')
            key_shift = ord(keyword_char) - ascii_value
            char_shift = ord(char) - ascii_value
            shift = (char_shift + key_shift) % 26

            encrypted_char = chr(shift + ascii_value)
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext


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
            if char.islower():
                ascii_value = ord('a')
            else:
                ascii_value = ord('A')
            key_shift = ord(keyword_char) - ascii_value
            char_shift = ord(char) - ascii_value
            shift = (char_shift - key_shift + 26) % 26

            decrypted_char = chr(shift + ascii_value)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


if __name__ == "__main__":
    PLAINTEXT = input("Enter a word: ")
    KEYWORD = input("Enter a keyword: ")
    CIPHERTEXT = encrypt_vigenere(PLAINTEXT, KEYWORD)

    print(f"Encrypted word: {CIPHERTEXT}")
    CIPHERTEXT = input("Enter cipher: ")
    KEYWORD = input("Enter keyword: ")
    PLAINTEXT = decrypt_vigenere(CIPHERTEXT, KEYWORD)

    print(f"Decrypted word: {PLAINTEXT}")
