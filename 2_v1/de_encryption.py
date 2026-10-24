from dict import alphabet, reverse_alphabet

def encryption(init_str, N, E):
    return [
        pow(int(reverse_alphabet[ch]), E, N)
        for ch in init_str
    ]

def decryption(encr_str, N, D):
    return "".join(
        alphabet[str(pow(int(num), D, N))]
        for num in encr_str
    )