

def find_multiple(initial_str: str):
    for i in range(2,1000):
        if len(initial_str) % i == 0:
            return i 