from newton_method import find_root_newton


def half_division():

    print("----------- Метод половинного деления ------------")
    a = -2
    b = 0.2953
    e = 0.001
    f = lambda x : 1.62*x**3 - 8.15*x**2 + 4.39*x + 4.29
    i = 0
    print(f"i\ta\tb\tx\tf(a)\tf(b)\t|a-b|")
    while(abs(a-b) > e):
        xi = (a + b) / 2
        print(f"{i}\t{round(a, 3)}\t{round(b, 3)}\t{round(xi, 3)}\t{round(f(a),3)}\t{round(f(b), 3)}\t{round(abs(a-b),3)}")
        if(f(xi)*f(a) > 0): a = xi
        else: b = xi
        i += 1
    print(f"calculation result: root={round((a+b)/2, 3)}")

def hord_method():

    print("----------- Метод хорд ------------")
    a = 3.0585
    b = 5
    e = 0.001
    f = lambda x : 1.62*x**3 - 8.15*x**2 + 4.39*x + 4.29
    i = 0
    xi = b
    print(f"i\ta\tb\tx\tf(a)\tf(b)\t|a-b|")
    while(abs(f(xi)) > e):
        xi = a - ((b-a)*f(a))/(f(b)-f(a))
        print(f"{i}\t{round(a, 3)}\t{round(b, 3)}\t{round(xi, 3)}\t{round(f(a),3)}\t{round(f(b), 3)}\t{round(abs(a-b),3)}")
        # print(f"|{i}\t|{round(a, 3)}\t|{round(b, 3)}\t|{round(xi, 3)}\t|{round(f(a),3)}\t|{round(f(b), 3)}\t|{round(abs(a-b),3)}|")
        if(f(xi)*f(a) > 0): a = xi
        else: b = xi
        i += 1
    print(f"calculation result: root={round(xi, 3)}")

def simple_iteration():
    print("----------- Метод простой итерации ------------")
    a = 2
    b = 4
    e = 0.001

    l = 100
    lambd =  1/(250871/48600)
    f = lambda x : 1.62*x**3 - 8.15*x**2 + 4.39*x + 4.29
    phi = lambda x : x + lambd*(f(x))
    i = 0
    xi = b
    x_prev = xi + 2*e
    print(f"i\tx_(i-1)\tf(xi)\txi\tphi(x_prev)\t|a-b|")
    while(abs(xi - x_prev) > e):
        x_prev = xi
        xi = phi(xi)
        print(f"{i}\t{round(x_prev, 3)}\t{round(f(xi), 3)}\t{round(xi, 3)}\t{round(phi(x_prev),3)}\t{round(abs(xi - x_prev),3)}")
        # print(f"|{i}\t|{round(x_prev, 3)}\t|{round(f(xi), 3)}\t|{round(xi, 3)}\t|{round(phi(x_prev),3)}\t|{round(abs(xi - x_prev),3)}|")
        i += 1
    print(f"calculation result: root={round(xi, 3)}")

def newton_method():
    print("----------- Метод Ньютона ------------")
    a = 0
    b = 1
    e = 0.001
    f = lambda x : x**2 + 5*x + 3
    print(f"calculation result: root={round(find_root_newton(f, a, b, e), 3)}")

hord_method()
half_division()
simple_iteration()
newton_method()
