def is_primary(n: int) -> bool:
    if n < 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def calculate_prime(start: int) -> int:
    if start & 1 == 0:
        start += 1

    while not is_primary(start):
        start += 2

    return start


def gcd(a: int, b: int) -> int:
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b > a:
        gcd_, x, y = extended_gcd(b, a)
        return gcd_, y, x
    if b == 0:
        return a, 1, 0

    gcd_, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd_, x, y


def fast_pow(number: int, step: int, module: int) -> int:
    if step == 0:
        return 1
    if step & 1 == 1:
        return (number * fast_pow(number, step - 1, module)) % module
    res_ = fast_pow(number, step // 2, module)
    return (res_ * res_) % module
