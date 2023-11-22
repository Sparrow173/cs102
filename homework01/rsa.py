"""
RSA Шифрование
"""
import random
import typing as tp


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    count = 2
    if n <= 1:
        return False
    while count <= n**0.5:
        if n % count == 0:
            return False
        count += 1
    return True


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    d = pow(e, -1, phi)
    return d


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:  # noqa
    """
    Генерация ключей для RSA шифрования
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char**key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    if is_prime(n) is True:
        print("True")
    else:
        print("False")

    A = int(input("Enter a: "))
    B = int(input("Enter b: "))
    GCD_NUM = gcd(A, B)
    if GCD_NUM == 1:
        print(f"gcd for a and b: {GCD_NUM}")

    E = int(input("Enter e: "))
    PHI = int(input("Enter phi: "))
    MULTIPLICATIVE_INVERSE_NUM = pow(E, PHI)
    print()

    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    PUBLIC, PRIVATE = generate_keypair(p, q)
    print("Your public key is ", PUBLIC, " and your private key is ", PRIVATE)
    MESSAGE = input("Enter a message to encrypt with your private key: ")
    ENCRYPTED_MSG = encrypt(PRIVATE, MESSAGE)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), ENCRYPTED_MSG)))
    print("Decrypting message with public key ", PUBLIC, " . . .")
    print("Your message is:")
    print(decrypt(PUBLIC, ENCRYPTED_MSG))
