from interals_counting.rectangles_method import calculate_integral_rectangles_method
from interals_counting.trapeze_method import calculate_integral_trapeze_method
from interals_counting.simpson_method import calculate_integral_simpson_method
from math import sin

start, stop = 0, 2
epsilon = 0.01
equation = lambda x: x**2 + 4*sin(x)

def main():
    calculate_integral_rectangles_method(equation, start, stop, epsilon)
    calculate_integral_trapeze_method(equation, start, stop, epsilon)
    calculate_integral_simpson_method(equation, start, stop, epsilon)

#Запускайте этот метод после получения числа интервалов (h) для каждого из методов в main()
def manual():
    print("----------- Метод Прямоугольников ------------")
    num_of_intervals = 10
    # for i in range(n):

main()
# manual()