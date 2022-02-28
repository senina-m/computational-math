import numpy as np
from scipy.misc import derivative


def find_root_simple_iteration(f, start, stop, epsilon):
    l = find_lambda(f, start, stop)
    q = find_q(f, start, stop)
    print(f"lambde={l}, q={q}")

    phi = lambda x: x + f(x)*l

    if(q > 0.5): check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) > epsilon
    else: check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) >= (1-q/q)*epsilon

    x0 = start
    x1 = phi(x0)

    xi = x1
    xi_prev = x0

    while(check(epsilon, xi, xi_prev, q)):
        print(f"xi={xi}, phi(xi)={phi(xi)}")
        tmp = xi
        xi = phi(xi_prev)
        xi_prev = tmp

    return xi




def find_lambda(f, start, stop):
    max_derivative = derivative(f, start, n=1)
    for i in np.arange(start, stop, 0.01):
        if max_derivative < derivative(f, i, n=1):
            max_derivative = derivative(f, i, n=1)
    return -1/max_derivative


def find_q(f, start, stop):
    max_derivative = derivative(f, start, n=1)
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, n=1)):
            max_derivative = abs(derivative(f, i, n=1))
    return max_derivative
