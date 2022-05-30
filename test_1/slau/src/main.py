from gauss import  count_result
from gauss_zeydel import gauss_zeydel
from simple_iteration import simple_iteration

#СЛАУ
matrix = [[0, 9, -1, -14], 
          [8, -2, 5, 12],
          [-3, -7, 1, 7]]
e = 0.0000001

# Решение слау методом Гаусса
# print(f"Gauss result = {count_result(matrix)}")
# Найти определитель методом Гаусса
# https://math.semestr.ru/gauss/opred.php

# Решение слау методом Гаусса с выбором главного элемента
# print(f"Gauss result = {count_result(matrix)}")

matrix = [[10, 1, 1, 12],
          [2, 10, 1, 13],
          [2, 2, 10, 14]]
# Решение слау методом Гаусса-Зейделя
print(f"Gauss-Zeydel result = {gauss_zeydel(matrix, e)}")

# Решение слау методом простой итерации
# print(f"simple_iteration result = {[round(i,3) for i in simple_iteration(matrix, e)]}")