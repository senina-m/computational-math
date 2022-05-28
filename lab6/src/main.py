from get_data import get_data
from plot import plot_result
from plot import plot_both_results
from runge_kutta import runge_kutta_differentiation
from milan import milan_differentiation
from math import sin, exp, log2, sqrt

def main():
    # f, initial_conditions, h, bounds, accuracy, method = get_data()
    # f = lambda x, y : 1/sqrt(x**2 - 1)
    # result_f = lambda x :  log2(abs(x + sqrt(x**2 - 1)))
    # initial_conditions = 0
    f = lambda x, y : exp(-3*x)
    result_f = lambda x :  -1/3*exp(-3*x) + 1
    initial_conditions = 2/3
    h = 0.3
    bounds = [0, 2]
    accuracy = 0.0001
    # result, x = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
    result_milan, x = milan_differentiation(f, initial_conditions, h, bounds, accuracy)
    result_runge_kutta, x = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
    print("=============results=============")
    print(f"milan\t\t{[round(i, 5) for i in result_milan]}")
    print(f"runge_kutta\t{[round(i, 5) for i in result_runge_kutta]}")
    print(f"Real values\t{[round(result_f(i), 5) for i in x]}")
    method = "both"
        
    match (method):
        case "runge–kutta":
            result, x = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
            plot_result(f, x, result, method)
        case "milan":
            result, x = milan_differentiation(f, initial_conditions, h, bounds, accuracy)
            plot_result(f, x, result, method)
        case "both":
            rungekutta_result, x = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
            milan_result, x = milan_differentiation(f, initial_conditions, h, bounds, accuracy)
            plot_both_results(f, x, milan_result, rungekutta_result)
        case _:
            print("Error in getting data from user!")
main()