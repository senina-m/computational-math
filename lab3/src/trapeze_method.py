import math
from scipy.misc import derivative
import numpy as np

def calculate_integral_trapeze_method(f, start, stop, e):
    # way to count interval width with given accuracy 
    # interval_width = (stop - start) / count_num_of_intervals(f, start, stop, e)
    num_of_intervals = 6
    result = (sum([f(i) for i in np.arange(start, stop - interval_width(start, stop, num_of_intervals), e / 2)]) + (start + stop) / 2) * interval_width
    prev_result = float(math.inf)
    while(math.abs(result - prev_result) / 3 > e):
        num_of_intervals *= 2
        prev_result = result
        result = (sum([f(i) for i in np.arange(start, stop - interval_width(start, stop, num_of_intervals), e / 2)]) + (start + stop) / 2) * interval_width
    print(f"sum for start:{result}")

def interval_width(start, stop, num_of_intervals):
    return (stop - start) / num_of_intervals

def count_num_of_intervals(f, start, stop, e):
    return math.sqrt(find_max_snd_derivative(f, start, stop)*(stop - start)**3/(12*e))

def find_max_snd_derivative(f, start, stop):
    max = derivative(f, start, n=2)
    for i in np.arange(start, stop, 0.01):
        if(derivative(f, i, n=2) > max):
            max = derivative(f, i, n=2)
    return round(max) + 1
