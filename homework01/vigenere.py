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
                ascii = 97
            else:
                ascii = 65
            key_shift = ord(keyword_char) - ascii
            char_shift = ord(plain_char) - ascii
            encrypted_shift = (key_shift + char_shift) % 26

            encrypted_char = chr(encrypted_shift + ascii)
            ciphertext += encrypted_char
        else:
            ciphertext += plaintext[i]

    return ciphertext


plaintext = input("Введите слово для шифрования: ")
keyword = input("Введите ключ-слово: ")
ciphertext = encrypt_vigenere(plaintext, keyword)

print(f"Зашифрованный текст: {ciphertext}")


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
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            keyword_char = keyword[i % len(keyword)]
            cipher_char = ciphertext[i]
            if ciphertext[i].islower():
                ascii = 97
            else:
                ascii = 65
            key_shift = ord(keyword_char) - ascii
            char_shift = ord(cipher_char) - ascii
            shift = (char_shift - key_shift + 26) % 26

            decrypted_char = chr(shift + ascii)
            plaintext += decrypted_char
        else:
            plaintext += ciphertext[i]

    return plaintext


ciphertext = input("Введите слово для расшифровки: ")
keyword = input("Введите ключ-слово: ")
plaintext = decrypt_vigenere(ciphertext, keyword)

print(f"Расшифрованный текст: {plaintext}")
