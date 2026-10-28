from dict import alphabet, reverse_alphabet

def encryption(init_str, n, e):
    return [
        pow(int(reverse_alphabet[ch]), e, n)
        for ch in init_str
    ]

def decryption(encr_str, n, d):
    return "".join(
        alphabet[str(pow(int(num), d, n))]
        for num in encr_str
    )
