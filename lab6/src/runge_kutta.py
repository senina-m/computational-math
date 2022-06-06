from decimal import Decimal
import numpy as np
from math import ceil

def runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy):
    n = ceil((bounds[1] - bounds[0])/ h) + 1 # здесь добавляется 1, чтобы количество точек было правильным (у k интервалов k+1 конец)
    # print(f"bounds=[{bounds[0]}, {bounds[1]}], diff={bounds[1]-bounds[0]}, h={h}, n={n}")
    # для этих иксов нужно предсказать значение y
    x = [bounds[0] + h*i for i in range(n)]
    y = [0]*(n)
    hes = [0]*(n) # ширина интервала для необходимой точности
    y[0] = initial_conditions
    
    for i in range(n - 1):
        local_bounds = [x[i], x[i + 1]]
        local_h = 1.0
        local_init_y = y[i]
        # print(f"interval [{round(local_bounds[0], 3)}, {round(local_bounds[1], 3)}], h={local_h}, y{i}={round(local_init_y, 3)}")
        y_n = runge_kutta(f, local_init_y, local_h, local_bounds)
        y_2n = runge_kutta(f, local_init_y, local_h/2, local_bounds)

        while abs(y_n - y_2n) / (2**(-fexp(accuracy)) - 1) > accuracy:
            # print(f"local_h={local_h}, y_2n={round(y_2n, 3)}, y_n={round(y_n, 3)}, R={round(abs(y_2n - y_n)/(2**(-fexp(accuracy)) - 1) , 4)}, (accuracy)={accuracy}")
            local_h /= 2
            y_n = runge_kutta(f, local_init_y, local_h, local_bounds)
            y_2n = runge_kutta(f, local_init_y, local_h/2, local_bounds)
            
        y[i + 1] = y_2n
        hes[i + 1] = local_h
    return y, x, hes


def runge_kutta(f, initial_conditions, h, bounds):
    n = ceil((bounds[1] - bounds[0]) / h) + 1
    x = [bounds[0] + h*i for i in range(n)]

    k_table = [[0]*4 for _ in range(n)] 
    #predicted val
    y = [0]*n
    y[0] = initial_conditions
    # print(f"\nn\txi\tyi\tk0\tk1\tk2\tk3\tf(x)")
    for i in range(n - 1):
        k_table[i][0] = h * f(x[i], y[i])
        k_table[i][1] = h * f(x[i] + h/2, y[i] + k_table[i][0]/2)
        k_table[i][2] = h * f(x[i] + h/2, y[i] + k_table[i][1]/2)
        k_table[i][3] = h * f(x[i] + h, y[i] + k_table[i][2])
        y[i+1] = y[i] + 1/6*(k_table[i][0] + 2 * k_table[i][1] + 2 * k_table[i][2] + k_table[i][3])
        # print(f"{i}\t{round(x[i], 3)}\t{round(y[i], 3)}\t{round(k_table[i][0], 3)}\t{round(k_table[i][1], 3)}\t{round(k_table[i][2], 3)}\t{round(k_table[i][3], 3)}\t{round(f(x[i], y[i]),3)}")
    return y[-1]

def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1