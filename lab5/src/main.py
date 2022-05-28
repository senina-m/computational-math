from get_data import get_data
from newton import newton_interpolation
from lagrange import lagrange_interpolation
from plot import plot_result
from plot import plot_both_results


def main():
    data, method, point = get_data()
    x = data["x"]
    y = data["y"]

    # x = [0.1, 0.2, 0.3, 0.4, 0.5]
    # y = [1.25, 2.38, 3.97, 5.44, 7.14]
    # method = "lagrange"
    # point = 0.15

    
    match (method):
        case "newton":
            result = newton_interpolation(x, y, point)
            plot_result(x, y, point, result)
        case "lagrange":
            result = lagrange_interpolation(x, y, point)
            plot_result(x, y, point, result)
        case "both":
            lagrange = lagrange_interpolation(x, y, point)
            newton = lagrange_interpolation(x, y, point)
            plot_both_results(x, y, point, lagrange, newton)
        case _:
            print("Error in getting data from user!")
    

main()