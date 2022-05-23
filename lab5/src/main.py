from get_data import get_data
from newton import newton_interpolation
from lagrange import lagrange_interpolation
from plot import plot_result


def main():
    # data, method, point = get_data()
    # x = data["x"]
    # y = data["y"]
    x = [2, 2.3, 2.6, 3]
    y = [2, 3, 5, 6]
    method = "newton"
    point = 60
    match (method):
        case "newton":
            result = newton_interpolation(x, y, point)
        case "lagrange":
            result = lagrange_interpolation(x, y, point)
        case _:
            print("Error in getting data from user!")
    plot_result(x, y, point, result)

main()