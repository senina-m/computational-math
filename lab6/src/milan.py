from runge_kutta import runge_kutta_differentiation
from math import ceil

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
    for i in range(4, n):
        finite_differences = count_finite_differences_const_h(y, i)
        # [print(arr) for arr in finite_differences]
        y_prediction = prediction(finite_differences, y, i, h)
        y_correction = correction(finite_differences, x, y, i, h, f, y_prediction)
        # print(f"prediction={round(y_prediction, 3)}, correction={round(y_correction, 3)} ")
        while abs(y_correction - y_prediction) > accuracy:
            y_prediction = y_correction
            y_correction = correction(finite_differences, x, y, i, h, f, y_correction)
            # print(f"prediction={round(y_prediction, 3)}, correction={round(y_correction, 3)} ")
        y[i] = y_correction
        # print(f"y[{i}]={round(y_correction, 3)}")
    return y, x
    #  0  1  2  3  4  5
    # [0, 1, 2, 3       ] fd

def prediction(fd, y, i, h):
    return y[i - 4] + 4*h/3 * (2*fd[0][i - 3] - fd[0][i - 2] + 2*fd[0][i - 1])

def correction(fd, x, y, i, h, f, y_pred):
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
