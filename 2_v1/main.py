from get_N_phi_E_D import get_p_q_N_E_D
from de_encryption import encryption, decryption
import os
import time
import json


def main():
    try:
        print(f"{os.getlogin()}: start session")
    except OSError:
        pass

    time.sleep(0.2)
    print("key generation")
    time.sleep(0.2)
    print("generation: N, phi_N, E, D")

    p, q, N, E, D = get_p_q_N_E_D()

    time.sleep(0.2)
    print("Generation was successful")
    time.sleep(0.2)

    while True:
        command = input("~>").strip()

        if command in ("keys", "-k"):
            print(f"p: {p}\nq: {q}\nN: {N}\nE: {E}\nD: {D}")

        elif command in ("encr", "-e"):
            init_str = input("~>")
            print(encryption(init_str, N, E), "\n")

        elif command in ("decr", "-d"):
            init_str = input("~>")
            try:
                encr_str = json.loads(init_str.strip('"'))
                print(decryption(encr_str, N, D), "\n")
            except (ValueError, KeyError, TypeError):
                print("Invalid ciphertext\n")

        elif command in ("full", "-f"):
            init_str = input("~>")
            encr_str = encryption(init_str, N, E)
            print("Encrypted:", encr_str)
            print("Decrypted:", decryption(encr_str, N, D),"\n")
            

        elif command in ("exit", "quit", "-q"):
            print("end of session")
            break

        else:
            print("Unknown command. Available: keys, -k, encr, -e, decr, -d, full, -f, exit")







if __name__ == "__main__":
    main()