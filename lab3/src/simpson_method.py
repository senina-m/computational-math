import math
from scipy.misc import derivative
import numpy as np

def calculate_integral_simpson_method(f, a, b, e):
    num_of_intervals = 4
    h = count_interval_width(a, b, num_of_intervals)
    odd_sum = count_odd_sum(f, a, b, num_of_intervals)
    even_sum = count_even_sum(f, a, b, num_of_intervals)

    result = h/3 * (f(a) + 4 * odd_sum + 2 * even_sum + f(b))
    prev_result = float('inf')
    while(abs(result - prev_result)/15 > e):
        prev_result = result
        num_of_intervals *= 2
        h = count_interval_width(a, b, num_of_intervals)
        odd_sum = count_odd_sum(f, a, b, num_of_intervals)
        even_sum = count_even_sum(f, a, b, num_of_intervals)
        result = h/3 * (f(a) + 4 * odd_sum + 2 * even_sum + f(b))

    print(f"simpson integral={result}, while the number of intervals was={num_of_intervals}")

def count_even_sum(f, a, b, num_of_intervals):
    h = count_interval_width(a, b, num_of_intervals)
    return sum([f(i) for i in np.arange(a + h, b, 2*h)])

def count_odd_sum(f, a, b, num_of_intervals):
    h = count_interval_width(a, b, num_of_intervals)
    return sum([f(i) for i in np.arange(a + 2*h, b, 2*h)])

def count_interval_width(a, b, num_of_intervals):
    return abs(b-a) / num_of_intervals