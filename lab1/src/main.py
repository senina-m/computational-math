from input import read_from_stdin
from input import read_from_file
from gauss_calculation import count_result

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

result = count_result(matrix)
print(result)
