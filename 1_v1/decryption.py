from utils import find_multiple

def fill_matrix_discryption(initial_str:str):
    number_columns = find_multiple(initial_str)
    matrix = []
    cut_length = len(initial_str)//number_columns
    for i in range(number_columns):
        current_str = initial_str[:cut_length]
        initial_str = initial_str[cut_length:]
        matrix.append(current_str)

    return matrix

def str_decryption(initial_str):
    matrix = fill_matrix_discryption(initial_str)
    decryption_str = ""
    for i in range(len(matrix[1])):
        for x in matrix:
            decryption_str += x[i]

    print(decryption_str.replace("*", ""))