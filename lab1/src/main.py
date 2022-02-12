import imp
from input import read_from_stdin
from input import read_from_file
from gauss_calculation import count_result, print_matrix
from gauss_calculation import count_matrix_det
from gauss_calculation import count_residual_vector
from gauss_calculation import validate_matrix
from gauss_calculation import print_matrix
import numpy as np

# Вычисление определителя
# Вывод треугольной  матрицы (включая преобразованный столбец В)
# Вывод вектора неизвестных: x1,  x2,  …, xn
# Вывод вектора невязок: r1,  r,  …, rn

filename = input("Read data from file? (y/n)")
matrix = []

if (filename == "n"):
    matrix = read_from_stdin()
elif (filename == "y"):
    matrix = read_from_file(filename)


validate_matrix(matrix)

det = count_matrix_det([line[:-1] for line in matrix])
print(f"Matrix det:{round(det, 3)}")
# print(f"Numpy det:{round(np.linalg.det(np.array([line[:-1] for line in matrix])), 3)}")

solution = count_result(matrix)
print(f"Matrix solution:{solution}")
# print(f"Numpy mattix solution:{np.linalg.solve([line[:-1] for line in matrix], [line[len(line) - 1] for line in matrix])}")

residual_vector = count_residual_vector(matrix, solution)
print(f"Residual vector:{residual_vector}")
