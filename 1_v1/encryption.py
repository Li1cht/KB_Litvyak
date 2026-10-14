from utils import find_multiple, is_prime



def fill_matrix_encryption(initial_str:str, number_columns: int):
    matrix = []
    for step in range(number_columns):
        new_str = ""
        initial_str_len = len(initial_str)

        for ch in range(step,initial_str_len,number_columns):
            new_str += initial_str[ch]

        matrix.append(new_str)
    return matrix



def str_encryption(initial_str:str):
    number_columns = find_multiple(initial_str)
    if is_prime(len(initial_str)):
        initial_str += "*"
        number_columns = find_multiple(initial_str)
        matrix = fill_matrix_encryption(initial_str, number_columns)
        print("".join(matrix))
        return ...


    matrix = fill_matrix_encryption(initial_str, number_columns)
    print("".join(matrix))
    return ...

