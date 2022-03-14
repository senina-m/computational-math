import math
from scipy.misc import derivative
import numpy as np

from lab3.src.trapeze_method import interval_width

def calculate_integral_rectangles_method(f, a, b, e):
    result_start, num_of_intervals_start = count_integral_start(f, a, b, e)
    result_middle, num_of_intervals_middle = count_integral_middle(f, a, b, e)
    result_stop, num_of_intervals_stop = count_integral_stop(f, a, b, e)
    print(f"start integral={result_start}, with num of intervals={num_of_intervals_start}")
    print(f"middle integral={result_middle}, with num of intervals={num_of_intervals_middle}")
    print(f"stop integral={result_stop}, with num of intervals={num_of_intervals_stop}")

def count_integral_start(f, a, b, e):
    result_start = lambda a, b, h : sum([f(i) for i in np.arange(a, b, h)]) * h
    return count_integral(result_start, f, a, b, e)

def count_integral_middle(f, a, b, e):
    result_start = lambda a, b, h : sum([f(i) for i in np.arange(a + h/2, b, h)]) * h
    return count_integral(result_start, f, a, b, e)

def count_integral_stop(f, a, b, e):
    result_start = lambda a, b, h : sum([f(i) for i in np.arange(a + h, b, h)]) * h
    return count_integral(result_start, f, a, b, e)


def count_integral(result_formula, f, a, b, e):
    num_of_intervals = 6
    h = interval_width(a, b, num_of_intervals)

    result = result_formula(a, b, h)
    prev_result = float(math.inf)
    while(math.abs(result - prev_result) / 3 > e):
        num_of_intervals *= 2
        h = interval_width(a, b, num_of_intervals)
        prev_result = result
        result = result_formula(a, b, h)
    return result, num_of_intervals

def interval_width(a, b, num_of_intervals):
    return (b - a) / num_of_intervals

#count accuracy by 2nd derivative

def count_num_of_intervals(f, a, b, e):
    return math.sqrt(find_max_snd_derivative(f, a, b)*(b - a)**3/(12*e))

def find_max_snd_derivative(f,a, b):
    max = derivative(f, a, n=2)
    for i in np.arange(a, b, 0.01):
        if(derivative(f, i, n=2) > max):
            max = derivative(f, i, n=2)
    return round(max) + 1