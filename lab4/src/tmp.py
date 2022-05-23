import numpy as np
from approximation.tools.matrix import solve_matrix

import sys

sys.stdout.reconfigure(encoding='utf-8')

f = lambda x: 2*x/(x**4+7)
i = 0
x = []
y = []
print(f"        n &    x &      f(x) \\\\")

while i*0.2 <=2 :
    x.append(i*0.2)
    y.append(f(i*0.2))
    print(f"        {i} &    {round(i*0.2, 3)} &      {round(f(i*0.2),3)} \\\\")
    i += 1
print(f"\n----------Линейная апроксимация--------------")

sum_x = sum(x)
sum_x2 = sum([xi ** 2 for xi in x])
sum_y = sum(y)
sum_xy = sum([x[i] * y[i] for i in range(i)])

print(f"sum_x   sum_x2   sum_y   sum_xy   n")
print(f"{round(sum_x , 3)} \t {round(sum_x2, 3)} \t {round(sum_y, 3)} \t {round(sum_xy, 3)}   {i}")
print(f"\n------------------------")
print()


matrix= [[sum_x2, sum_x, sum_xy],
        [sum_x, i, sum_y]]
[print(f"{round(i[0],3)} \t {round(i[1],3)} \t {round(i[2],3)}") for i in matrix]

print(f"\n------------------------")

r = solve_matrix(matrix)
print(f"a \t{round(r[1], 3)}")
print(f"b \t{round(r[0], 3)}")

print(f"\n----------Кввадратичная апроксимация--------------")

sum_x3 = sum([xi ** 3 for xi in x])
sum_x4 = sum([xi ** 4 for xi in x])
sum_x2y = sum([(x[i] ** 2) * y[i] for i in range(i)])

print(f"sum_x\tsum_x2\tsum_x3\tsum_x4\tsum_y\tsum_xy\tsum_x2y\tn")
print(f"{round(sum_x , 3)}\t{round(sum_x2, 3)}\t{round(sum_x3, 3)}\t{round(sum_x4, 3)}\t{round(sum_y, 3)}\t{round(sum_xy, 3)}\t{round(sum_x2y, 3)}\t{i}")
print(f"\n------------------------")
print()

matrix =[[i, sum_x, sum_x2, sum_y],
        [sum_x, sum_x2, sum_x3, sum_xy],
        [sum_x2, sum_x3, sum_x4, sum_x2y]]
[print(f"{round(i[0],3)} \t {round(i[1],3)} \t {round(i[2],3)} \t {round(i[3],3)}") for i in matrix]
print(f"\n------------------------")

r = solve_matrix(matrix)
print(f"a \t{round(r[0], 3)}")
print(f"b \t{round(r[1], 3)}")
print(f"c \t{round(r[2], 3)}")


