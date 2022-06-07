from runge_kutta import runge_kutta_differentiation
from math import ceil
import numpy as np

def milan_differentiation(f, initial_conditions, h, bounds, accuracy):
    n = ceil((bounds[1] - bounds[0]) / h) + 1 # здесь добавляется 1, чтобы количество точек было правильным (у k интервалов k+1 конец)
    if (n < 4):
        print("For Milan differentiation num of intervals has to be at least 4!")
        print(f"h = {h}, on  ({bounds[0]}, {bounds[1]}), n = ceil((bounds[1] - bounds[0])/ h) + 1 = {n}")
        exit(0)
    # для этих иксов нужно предсказать значение y
    x = [bounds[0] + h*i for i in range(n)]
    # print("_____________Count Runge-Kutta________________")
    y = [0]*(n)
    runge_result, runge_x, hes = runge_kutta_differentiation(f, initial_conditions, h, [x[0], x[3]], accuracy)
    for i in range(4):
        y[i] = runge_result[i]
    # print(y)
    # print("_____________Count Milan________________")
    print(f"predict\t\t\tcorrect\t\t\tdiff\t\taccuracy")
    for i in range(4, n):
        finite_differences = count_finite_differences_const_h(y, i)
        [print(np.round(arr, 3)) for arr in finite_differences]
        print(f"===== i={i} x={round(x[i], 3)} =====================")
        print(f"y = {np.round(y, 3)}")
        print(f"x = {np.round(x, 3)}")


        y_prediction = prediction(finite_differences, y, i, h)
        y_correction = correction(finite_differences, x, y, i, h, f, y_prediction)
        print(f"f(x, y_pr)={round(f(x[i], y_prediction), 8)}, {round(y_prediction, 5)}")
        print(f"f(x, y_corr)={round(f(x[i], y_correction), 8)}, {round(y_correction, 5)}")

        # print(f"{round(y_prediction, 6)}\t\t{round(y_correction, 6)}\t\t{round(abs(y_correction - y_prediction), 3)}\t\t{accuracy}")

        while abs(y_correction - y_prediction) > accuracy:
            y_prediction = y_correction
            y_correction = correction(finite_differences, x, y, i, h, f, y_correction)

            # print(f"{round(y_prediction, 6)}\t\t{round(y_correction, 6)}\t\t{round(abs(y_correction - y_prediction), 3)}\t\t{accuracy}")
        y[i] = y_correction
    return y, x

def prediction(fd, y, i, h):
    a = y[i - 4] + 4*h/3 * (2*fd[0][i - 3] + fd[0][i - 2] + 2*fd[0][i - 1])
    print(f"prediction = {round(y[i - 4], 3)} + 4*{round(h, 3)}/3 * (2*{round(fd[0][i - 3], 3)} + {round(fd[0][i - 2], 3)} + 2*{round(fd[0][i - 1], 3)})={round(a, 5)}")
    return y[i - 4] + 4*h/3 * (2*fd[0][i - 3] + fd[0][i - 2] + 2*fd[0][i - 1])

def correction(fd, x, y, i, h, f, y_pred):
    a = y[i - 2] + h/3*(fd[0][i - 2] + 4*fd[0][i - 1] + f(x[i], y_pred))
    print(f"correction = {round(y[i - 2], 3)} + {round(h, 3)}/3*({round(fd[0][i - 2], 3)} + 4*{round(fd[0][i - 1], 3)} + {round(f(x[i], y_pred), 3)}={round(a, 5)}")
    return y[i - 2] + h/3*(fd[0][i - 2] + 4*fd[0][i - 1] + f(x[i], y_pred))

def count_finite_differences_const_h(y, n):
    finite_differences = [[0]*n for _ in range(n)]
    for i in range(n):
        finite_differences[i][0] = y[i]

    k = 1
    while k <= n:
        for i in range(n-k):
            finite_differences[i][k] = finite_differences[i+1][k-1] - finite_differences[i][k-1]
        k += 1
    return finite_differences
