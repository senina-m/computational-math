from approximation.tools.matrix import solve_matrix
from approximation.tools.standart_deviation import variance, standard_deviation
import numpy as np

def cube_approximation(points):

    n = len(points)
    x = [dot[0] for dot in points]
    print(points)
    y = [dot[1] for dot in points]

    sum_x = sum(x)
    sum_x2 = sum([xi ** 2 for xi in x])
    sum_x3 = sum([xi ** 3 for xi in x])
    sum_x4 = sum([xi ** 4 for xi in x])
    sum_x5 = sum([xi ** 5 for xi in x])
    sum_x6 = sum([xi ** 6 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2y = sum([(x[i] ** 2) * y[i] for i in range(n)])
    sum_x3y = sum([(x[i] ** 3) * y[i] for i in range(n)])

# manual solving of matrix
#     matrix =[[sum_x3, sum_x2, sum_x, n, sum_y],
#             [sum_x4, sum_x3, sum_x2, sum_x, sum_xy],
#             [sum_x5, sum_x4, sum_x3, sum_x2, sum_x2y],
#             [sum_x6, sum_x5, sum_x4, sum_x3, sum_x3y]]
#     r = solve_matrix(matrix)

    matrix =[[n, sum_x, sum_x2, sum_x3, sum_y],
            [sum_x, sum_x2, sum_x3, sum_x4, sum_xy],
            [sum_x2, sum_x3, sum_x4, sum_x5, sum_x2y],
            [sum_x3, sum_x4, sum_x5, sum_x6, sum_x3y]]
    r = solve_matrix(matrix)
#     matrix =[[sum_x3, sum_x2, sum_x, n],
#             [sum_x4, sum_x3, sum_x2, sum_x],
#             [sum_x5, sum_x4, sum_x3, sum_x2],
#             [sum_x6, sum_x5, sum_x4, sum_x3]]

#     res = [sum_y, sum_xy, sum_x2y, sum_x3y]
#     r = np.linalg.solve(matrix, res)


    result = {}
    result['a_0'] = r[0]
    result['a_1'] = r[1]
    result['a_2'] = r[2]
    result['a_3'] = r[3]

    f = lambda i: r[3] * (i**3) + r[2] * (i**2) + r[1] * i + r[0]
    print([f(i) for i in x])
    result['function'] = f
    result['string_function'] = f"{round(r[3], 3)}x^3 + {round(r[2], 3)}x^2 + {round(r[1], 3)}*x + {round(r[0], 3)}"
    result['variance'] = variance(points, f)
    result['standard_deviation'] = standard_deviation(points, f)

    return result
