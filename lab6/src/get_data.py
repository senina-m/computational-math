from math import sin

def get_data():
    print("Choose function:")
    print("1 ----------------- f(x, y) = x^2 + y^2")
    print("2 ----------------- f(x, y) = 1/xy")
    print("3 ----------------- f(x, y) = y*sin(x)")
    while True:
        try:
            choose_data_method = int(input())
            match (choose_data_method):
                case 1:
                    f =  lambda x, y : x**2 + y**2
                    break
                case 2:
                    f = lambda x, y : 1 / x * y
                    break
                case 3:
                    f = lambda x, y : y * sin(x)
                    break
                case _:
                    print("Enter your choice again!")
        except ValueError:
            print("Value has be integer! Try again from new line...")
    
    print("Enter the initial conditions as y(x_0)= ...")
    while True:
        try:
            initial_conditions = float(input())
            break
        except ValueError:
            print("Value has be float! Try again from new line...")

    print("Enter segment's bounds (enter the values separated by a space):")
    while True:
        try:
            values = input().strip().split()
            [float(i) for i in values]
            if(len(values) == 2):
                bounds = (max(values[0], values[1]), min(values[0], values[1]))
                break
            else:
                print("Wrong format! Try again from new line...")
        except ValueError:
            print("Both values has be float! Try again from new line...")
    
    print("Enter accuracy:")
    while True:
        try:
            accuracy = float(input())
            if 0 < accuracy and accuracy <= 1:
                break
            else:
                print("Value has to be in (0;1]. Try again from new line...")
        except ValueError:
            print("Value has be float! Try again from new line...")

    print("Enter length of intervals h:")
    while True:
        try:
            h = int(input())
            if h < bounds[1] - bounds[0]:
                print("Length of intervals must be less than entered interval! Try again from new line..")
            else:
                break
        except ValueError:
            print("Value has be integer! Try again from new line...")
    
    print("Choose method:")
    print("1 ----------------- Runge–Kutta method")
    print("2 ----------------- Milan method")
    # print("3 ----------------- both method")
    while True:
        try:
            choose_data_method = int(input())
            match (choose_data_method):
                case 1:
                    method =  "runge–kutta"
                    break
                case 2:
                    method = "milan"
                    break
                # case 3:
                    # method = "both"
                    # break
                case _:
                    print("Enter your choice again!")
        except ValueError:
            print("Value has be integer! Try again from new line...")
      
    return f, initial_conditions, h, bounds, accuracy, method


