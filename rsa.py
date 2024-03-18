import random
from collections import namedtuple

from math_func import calculate_prime, extended_gcd, gcd, fast_pow

PublicKey = namedtuple('PublicKey', ['e', 'n'])
PrivateKey = namedtuple('PrivateKey', ['d', 'n'])


def calculate_two_prime_numbers() -> tuple[int, int]:
    start = random.randint(10001, 1000001)

    first_prime = calculate_prime(start)
    second_prime = calculate_prime(first_prime + 2)

    return first_prime, second_prime


def calculate_d(m: int) -> int:
    start = random.randint(2, m)

    while gcd(m, start) != 1:
        start += 1

    return start


def calculate_e(d: int, m: int) -> int:
    _, x, y = extended_gcd(d, m)

    while x < 0:
        x += m
    return x


def calculate_keys() -> tuple[PublicKey, PrivateKey]:
    p, q = calculate_two_prime_numbers()

    n = p * q
    m = (p - 1) * (q - 1)

    d = calculate_d(m)
    e = calculate_e(d, m)

    return PublicKey(e, n), PrivateKey(d, n)


def encrypt(message: int, public_key: PublicKey) -> int:
    return fast_pow(message, public_key.e, public_key.n)


def decrypt(message: int, private_key: PrivateKey) -> int:
    return fast_pow(message, private_key.d, private_key.n)
