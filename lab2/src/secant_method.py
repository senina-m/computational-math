
from newton_method import check_interval
from newton_method import choose_x0
from scipy.misc import derivative


def find_root_scant(f, start, stop, epsilon):
    if not check_interval(f, start, stop): return None
    x0 = choose_x0(f, start, stop)
    x1 = x0  - f(x0) / derivative(f, x0, n=1)

    xi = x1
    xi_prev = x0
    while(abs(xi - xi_prev) > epsilon):
        tmp = xi
        xi = xi - f(xi) * (xi - xi_prev) / (f(xi) - f(xi_prev))
        xi_prev = tmp
    return xi

