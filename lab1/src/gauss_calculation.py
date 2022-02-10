import sys

# TODO:clean up prints

def validate_matrix(matrix):

    if(matrix == []):
        print("Input data is empty")
        sys.exit(1)
    n = len(matrix)

    for line in matrix:
        if len(line) - 1 != n:
            print("Invalide amount of numbers in lines")
            sys.exit(1)
    return n

def print_matrix(matrix):
    for line in matrix:
            print(line)


def swap_lines(matrix, i):
    for j in range(i + 1, len(matrix)):
        if(matrix[j][i] != 0):
            matrix[j], matrix[i] = matrix[i], matrix[j]
            return matrix
    print("System has no uniq splution!")
    print_matrix(matrix)
    sys.exit(0)


def count_result(matrix):
    n = validate_matrix(matrix)
    print_matrix(matrix)
    for i in range(0, n):

        if(matrix[i][i] == 0):
            matrix = swap_lines(matrix, i)

        i_i = matrix[i][i]
        for j_in_i_line in range(i, n + 1):
            matrix[i][j_in_i_line] = matrix[i][j_in_i_line]/i_i

        for j_after_i in range(i + 1, n):
            j_line_head = matrix[j_after_i][i]
            for k in range(i, n + 1):
                matrix[j_after_i][k] = matrix[j_after_i][k] - j_line_head*matrix[i][k]


    for i in range(1, n):
        for j_before_i in range(0, i):
            i_head = matrix[j_before_i][i]
            for k in range(i, n + 1):
                matrix[j_before_i][k] = matrix[j_before_i][k] - matrix[i][k]*i_head

    return [round(matrix[i][n], 3) for i in range(0, len(matrix))]
