import numpy as np
import matplotlib.pyplot as plt

from input_data import read_equation_console
from input_data import read_interval_console
from newton_method import find_root_newton

epsilon = 0.0001

equation = read_equation_console()
start, stop = read_interval_console()

root = find_root_newton(equation, start, stop, epsilon)
if root == None: print("Invalide interval and equation for Newton alculation method")
else:
    plt.plot([i for i in np.arange(start, stop, 0.01)], [equation(i) for i in np.arange(start, stop, 0.01)])
    plt.plot(root, equation(root), 'o')
    plt.title(f"Newton method. Root in [{start},{stop}]")
    plt.show()

