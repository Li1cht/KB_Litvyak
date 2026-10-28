from math import gcd
from secrets import randbelow

from utils import generate_prime

BIGIST = 52


def find_e(phi_N):
    while True:
        E = randbelow(phi_N - 2) + 2
        if gcd(E, phi_N) == 1:
            return E


def get_p_q_N_E_D():
    while True:
        p = generate_prime(BIGIST)
        q = generate_prime(BIGIST)

        while p == q:
            q = generate_prime(BIGIST)

        N = p * q
        phi_N = (p - 1) * (q - 1)
        break

    E = find_e(phi_N)
    D = pow(E, -1, phi_N)

    return p, q, N, E, D
