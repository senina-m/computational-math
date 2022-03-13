import math
from scipy.misc import derivative
import numpy as np

def calculate_integral_trapeze_method(f, start, stop, e):
    interval_width = (stop - start) / count_interval_width(f, start, stop, e)
    #h_i -- devide interval to epsilon parts
    sum = sum([f(i) for i in range(start, stop - interval_width, e/2)])
    print(f"sum for start:{(sum + (start + stop)/2)*interval_width}")

def count_interval_width(f, start, stop, e):
    return math.sqrt(find_max_snd_derivative(f, start, stop)*(stop - start)**3/(12*e))

def find_max_snd_derivative(f,start, stop):
    max = derivative(f, start, n=2)
    for i in np.arange(start, stop, 0.01):
        if(derivative(f, i, n=2) > max):
            max = derivative(f, i, n=2)
    return round(max) + 1
