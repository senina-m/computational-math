from get_data import get_data
from plot import plot_result
from plot import plot_both_results
from runge_kutta import runge_kutta_differentiation
from milan import milan_differentiation

def main():
    # f, f_result, initial_conditions, h, bounds, accuracy, method = get_data()
    f = lambda x, y : y + 2*x
    initial_conditions = 1
    h = 0.1

    bounds = [6, 10]
    x0 = bounds[0]
    y0= initial_conditions
    f_result = lambda x : 1/2*x + y0 - 2*x0
    accuracy = 0.0001
    method ="both"

    result_milan, x = milan_differentiation(f, initial_conditions, h, bounds, accuracy)
    result_runge_kutta, x, hes = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
    # plot_result(x, result_milan, [round(f_result(i), 4) for i in x], "milan")
    print("=============results=============")
    print(f"x\t\tmilan\t\trunge\t\trunge h\t\treal\t\t")
    for i in range(len(x)):
        print(f"{round(x[i], 3)}\t\t{round(result_milan[i], 4)}\t\t{round(result_runge_kutta[i], 5)}\t\t{round(hes[i], 5)}\t\t {round(f_result(i), 5)}")
    match (method):
        case "runge–kutta":
            plot_result(f_result, x, result_runge_kutta, method)
        case "milan":
            plot_result(f_result, x, result_milan, method)
        case "both":
            plot_both_results(f, x, result_milan, result_runge_kutta, [round(f_result(i), 4) for i in x])
        case _:
            print("Error in getting data from user!")
main()