from runge_kutta import runge_kutta_differentiation
from math import ceil
import numpy as np
import pandas as pd

def milan_differentiation(f, initial_conditions, h, bounds, accuracy):
    print("_____________________ MILAN _____________________________")
    n = ceil((bounds[1] - bounds[0]) / h) + 1 # здесь добавляется 1, чтобы количество точек было правильным (у k интервалов k+1 конец)
    if (n < 4):
        print("For Milan differentiation num of intervals has to be at least 4!")
        print(f"h = {h}, on  ({bounds[0]}, {bounds[1]}), n = ceil((bounds[1] - bounds[0])/ h) + 1 = {n}")
        exit(0)

    # для этих иксов нужно предсказать значение y
    x = [bounds[0] + h*i for i in range(n)]
    y = [0]*(n)


    # Вычисляем первые 4 значения y
    runge_result, runge_x, hes = runge_kutta_differentiation(f, initial_conditions, h, [x[0], x[3]], accuracy)
    for i in range(4):
        y[i] = runge_result[i]
    

    print(f"predict\t\t\tcorrect\t\t\tdiff\t\taccuracy")
    for i in range(4, n):
        fd = count_fd(y, i)
        print_fd(fd)
        print(f"===== i={i} x={round(x[i], 3)} =====================")
        # print(f"y = {np.round(y, 3)}")


        y_prediction = prediction(fd, h)
        y_correction = correction(fd, x, y, i, h, f, y_prediction)
        # print(f"{round(y_prediction, 6)}\t\t{round(y_correction, 6)}\t\t{round(abs(y_correction - y_prediction), 3)}\t\t{accuracy}")

        while abs(y_correction - y_prediction) > accuracy:
            y_prediction = y_correction
            y_correction = correction(fd, x, y, i, h, f, y_correction)

            print(f"{round(y_prediction, 6)}\t\t{round(y_correction, 6)}\t\t{round(abs(y_correction - y_prediction), 3)}\t\t{accuracy}")
        y[i] = y_correction
    print("_____________________ MILAN END _____________________________")
    return y, x

def prediction(fd, h):
    a = fd[0][0] + 4*h/3 * (2*fd[0][1] + fd[0][2] + 2*fd[0][3])
    # print(f"prediction = {round(fd[0][0], 3)} + 4*{round(h, 3)}/3 * (2*{round(fd[0][1], 3)} + {round(fd[0][2], 3)} + 2*{round(fd[0][3], 3)})={round(a, 5)}")
    return a

def correction(fd, x, y, i, h, f, y_pred):
    a = y[i - 2] + h/3*(fd[0][2] + 4*fd[0][2] + f(x[i], y_pred))
    # print(f"correction = {round(y[i - 2], 3)} + {round(h, 3)}/3*({round(fd[0][2], 3)} + 4*{round(fd[0][3], 3)} + {round(f(x[i], y_pred), 3)}={round(a, 5)}")
    return a

def count_fd(y, j):
    n = 4
    fd = [[0]*n for _ in range(n)]
    for i in range(n):
        fd[i][0] = y[j + i - 4]

    for k in range(1, n):
        for i in range(n-k):
            fd[i][k] = fd[i+1][k-1] - fd[i][k-1]
    return fd

def print_fd(fd):
    dataframe = pd.DataFrame(fd)
    print(dataframe)
