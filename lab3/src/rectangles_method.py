import math
from scipy.misc import derivative
import numpy as np

def calculate_integral_rectangles_method(f, start, stop, e):
    num_of_intervals = count_num_of_intervals(f, start, stop, e)
    interval_width = (stop - start) / num_of_intervals
    print(f"sum for start:{sum([f(i) for i in range(start, stop, num_of_intervals)])*interval_width}")
    print(f"sum for stop:{sum([f(i) for i in range(start + interval_width, stop, num_of_intervals)])*interval_width}")
    print(f"sum for middle:{sum([f(i) for i in range(start + interval_width/2, stop, num_of_intervals)])*interval_width}")

def count_num_of_intervals(f, start, stop, e):
    return math.sqrt(find_max_snd_derivative(f, start, stop)*(stop - start)**3/(12*e))

def find_max_snd_derivative(f,start, stop):
    max = derivative(f, start, n=2)
    for i in np.arange(start, stop, 0.01):
        if(derivative(f, i, n=2) > max):
            max = derivative(f, i, n=2)
    return round(max) + 1