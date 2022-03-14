import math
from scipy.misc import derivative
import numpy as np

def calculate_integral_trapeze_method(f, a, b, e):
    
    num_of_intervals = 6
    h = interval_width(a, b, num_of_intervals)
    result = (sum([f(i) for i in np.arange(a, b - h, e / 2)]) + (a + b) / 2) * h
    prev_result = float('inf')
    while(abs(result - prev_result) / 3 > e):
        num_of_intervals *= 2
        h = interval_width(a, b, num_of_intervals)
        prev_result = result
        result = (sum([f(i) for i in np.arange(a, b - h, e / 2)]) + (a + b) / 2) * h
    print(f"trapeze integral={result}, where num of inerval was={num_of_intervals}")

def interval_width(a, b, num_of_intervals):
    return abs(b - a) / num_of_intervals

#count accuracy by 2nd derivative

# way to count interval width with given accuracy 
# interval_width = (b - a) / count_num_of_intervals(f, a, b, e)
def count_num_of_intervals(f, a, b, e):
    return math.sqrt(find_max_snd_derivative(f, a, b)*(b - a)**3/(12*e))

def find_max_snd_derivative(f, a, b):
    max = derivative(f, a, n=2)
    for i in np.arange(a, b, 0.01):
        if(derivative(f, i, n=2) > max):
            max = derivative(f, i, n=2)
    return round(max) + 1
