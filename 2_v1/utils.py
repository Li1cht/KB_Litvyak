from secrets import randbelow


def is_probable_prime(n, rounds=20):
    if n < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

    for prime in small_primes:
        if n % prime == 0:
            return n == prime

    #n - 1 ~> d * 2**s
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    # Миллер — Рабин
    for _ in range(rounds):
        a = randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True



def generate_prime(digits):
    lower = 10 ** (digits - 1)
    upper = 10 ** digits
    while True:
        n = randbelow(upper - lower) + lower
        n |= 1
        if len(str(n)) == digits and is_probable_prime(n):
            return n