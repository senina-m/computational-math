from newton import newton_interpolation
x = [1.10, 1.25, 1.40, 1.55, 1.70, 1.85, 2.00]
y = [0.2234, 1.2438, 2.2644, 3.2984, 4.3222, 5.3516, 6.3867] 
x1 = 1.875
x2 = 1.575

result_x1 = newton_interpolation(x, y, x1)
print(result_x1)

result_x2 = newton_interpolation(x, y, x2)
print(result_x2)