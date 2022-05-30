from test_1.slau.src.gauss import print_matrix


def solve_minor(matrix, i, j):
    # Найти минор элемента матрицы
    n = len(matrix)
    return [[matrix[row][col] for col in range(n) if col != j] for row in range(n) if row != i]


def solve_det(matrix):
    # Найти определитель матрицы
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    sgn = 1
    for j in range(n):
        det += sgn * matrix[0][j] * solve_det(solve_minor(matrix, 0, j))
        sgn *= -1
    return det


def solve(matrix):
    # Метод Гаусса с выбором главного элемента по столбцам
    print(" _________________ Метод Гаусса с выбором главного элемента по столбцам _________________")
    n = len(matrix)
    det = solve_det([matrix[i][:n] for i in range(n)])
    if det == 0:
        return None

    # Прямой ход
    for i in range(n - 1):
        # Поиск максимального элемента в столбце
        max_i = i
        for m in range(i + 1, n):
            if abs(matrix[m][i]) > abs(matrix[max_i][i]):
                max_i = m

        # Перестановка строк
        if max_i != i:
            for j in range(n + 1):
                matrix[i][j], matrix[max_i][j] = matrix[max_i][j], matrix[i][j]

        # Исключение i-того неизвестного
        for k in range(i + 1, n):
            coef = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= coef * matrix[i][j]
        print_matrix("прямой ход", matrix)
        

    reduced_matrix = matrix[:]

    # Обратный ход
    roots = [0] * n
    for i in range(n - 1, -1, -1):
        s_part = 0
        for j in range(i + 1, n):
            s_part += matrix[i][j] * roots[j]
        roots[i] = (matrix[i][n] - s_part) / matrix[i][i]
        print_matrix("обратный ход", matrix)


    # Вычисление невязок
    residuals = [0] * n
    for i in range(n):
        s_part = 0
        for j in range(n):
            s_part += matrix[i][j] * roots[j]
        residuals[i] = s_part - matrix[i][n]
        print_matrix("вычисление невязок", matrix)

    print(" _________________ Метод Гаусса с выбором главного элемента по столбцам КОНЕЦ _________________")

    return det, reduced_matrix, roots, residuals