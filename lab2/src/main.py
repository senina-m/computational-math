import numpy as np
import matplotlib.pyplot as plt

from input_data import read_equation_console
from input_data import read_interval_console
from input_data import read_epsilon_console
from input_data import read_method

from newton_method import find_root_newton
from simple_iteration_method import find_root_simple_iteration
from secant_method import find_root_scant

equation = read_equation_console()
start, stop = read_interval_console()
epsilon = read_epsilon_console()
match read_method():
    case 1:
        root = find_root_newton(equation, start, stop, epsilon)
        if root == None: print("Invalide interval and equation for Newton calculation method")
    case 2:
        root = find_root_scant(equation, start, stop, epsilon)
        if root == None: print("Invalide interval and equation for scant calculation method")
    case 3:
        root = find_root_simple_iteration(equation, start, stop, epsilon)
        if root == None: print("Invalide interval and equation for simple iteration calculation method")

    case _:
        print("Error with choosing method!")

if root != None:
    print(f"root={root} in [{start}, {stop}]")
    plt.plot([i for i in np.arange(start, stop, 0.01)], [equation(i) for i in np.arange(start, stop, 0.01)])
    plt.plot(root, equation(root), 'o')
    plt.title(f"Root in [{start},{stop}]")
    plt.show()
exit(0)
