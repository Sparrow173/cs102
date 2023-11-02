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
    for letter in plaintext:
        if letter.isalpha():
            if letter.islower():
                ascii = 97
            else:
                ascii = 65
            encrypted_char = chr((ord(letter) - ascii + shift) % 26 + ascii)  # noqa
            ciphertext += encrypted_char
        else:
            ciphertext += letter
    return ciphertext


word = input("Введите слово для шифрования: ")

encrypted_word = encrypt_caesar(word)
print("Зашифрованное слово:", encrypted_word)


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
    for letter in ciphertext:
        if letter.isalpha():
            if letter.islower():
                ascii = 97
            else:
                ascii = 65
            decrypted_word = chr((ord(letter) - ascii - shift) % 26 + ascii)
            plaintext += decrypted_word
        else:
            plaintext += letter
    return plaintext


word = input("Введите зашифрованное слово для расшифровки: ")

decrypted_char = decrypt_caesar(word)
print("Расшифрованное слово:", decrypted_char)
