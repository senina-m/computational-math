import numpy as np
from scipy.misc import derivative


def find_root_simple_iteration(f, start, stop, epsilon):
    print("__________________simple iteration__________________")
    l = find_lambda(f, start, stop)
    q = find_q(f, start, stop)

    print(f"lambda={round(l, 5)}, q=={round(q, 5)}")

    phi = lambda x: x + f(x)*l
    print(f"phi(x) = x + f(x)*{round(l, 3)}")

    if(q > 0.5): check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) > epsilon
    else: check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) >= (1-q/q)*epsilon

    x0 = start
    x1 = phi(x0)

    xi = x1
    xi_prev = x0

    while(check(epsilon, xi, xi_prev, q)):
        tmp = xi
        xi = phi(xi_prev)
        xi_prev = tmp
    print("__________________simple iteration end__________________")

    return xi


def find_lambda(f, start, stop):
    max_derivative = abs(derivative(f, start, n=1))
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, n=1)):
            max_derivative = abs(derivative(f, i, n=1))
    return -1/max_derivative


def find_q(f, start, stop):
    max_derivative = derivative(f, start, n=1)
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, n=1)):
            max_derivative = abs(derivative(f, i, n=1))
    return max_derivative
