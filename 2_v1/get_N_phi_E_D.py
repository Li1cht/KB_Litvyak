from secrets import randbelow
from math import gcd
from utils import generate_prime

BIGIST = 52

def calculate_N(p, q):
    N = p*q
    return p*q

def calculate_phi(p,q):
    phi = (p-1)*(q-1)
    return phi

def find_e(phi_N):
    while True:
        E = randbelow(phi_N - 2) + 2
        if gcd(E, phi_N) == 1:
            return E

def find_d(phi_N, e):
    return pow(e, -1, phi_N)


def get_p_q_N_E_D():
    while True:
        p = generate_prime(BIGIST)
        q = generate_prime(BIGIST)

        if p == q:
            continue

        N = calculate_N(p, q)
        phi_N = calculate_phi(p, q)
        break


    E = find_e(phi_N)
    D = find_d(phi_N,E)

    return p, q, N, E, D

