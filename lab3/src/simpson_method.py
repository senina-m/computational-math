import numpy as np
from abstract_integral_rune_check import count_abstract_integral_rune_check

def calculate_integral_simpson_method(f, a, b, e):
    result_formula = lambda h: simpson_formula(h, a, b, f)
    result, num_of_intervals =  count_abstract_integral_rune_check(result_formula, a, b, e * 15)

    print(f"simpson integral={result}, while the number of intervals was={num_of_intervals}")

def simpson_formula(h, a, b, f):
    num_of_intervals = abs(b - a) / h
    odd_sum = count_odd_sum(f, a, b, num_of_intervals)
    even_sum = count_even_sum(f, a, b, num_of_intervals)
    return h/3 * (f(a) + 4 * odd_sum + 2 * even_sum + f(b))

def count_even_sum(f, a, b, num_of_intervals):
    h = count_interval_width(a, b, num_of_intervals)
    return sum([f(i) for i in np.arange(a + h, b, 2*h)])

def count_odd_sum(f, a, b, num_of_intervals):
    h = count_interval_width(a, b, num_of_intervals)
    return sum([f(i) for i in np.arange(a + 2*h, b, 2*h)])

def count_interval_width(a, b, num_of_intervals):
    return abs(b-a) / num_of_intervals