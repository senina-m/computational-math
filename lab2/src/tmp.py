def half_devidion():

    print("----------- Метод половинного деления ------------")
    a = -2
    b = 0.2953
    e = 0.001
    f = lambda x : 1.62*x**3 - 8.15*x**2 + 4.39*x + 4.29
    i = 0

    while(abs(a-b) > e):
        xi = (a + b) / 2
        # print(f"i={i} a={round(a, 3)} b={round(b, 3)} x={round(xi, 3)} f(a)={round(f(a),3)} f(b)={round(f(b), 3)} |a-b|={round(abs(a-b),3)}")
        print(f"|{i}\t|{round(a, 3)}\t|{round(b, 3)}\t|{round(xi, 3)}\t|{round(f(a),3)}\t|{round(f(b), 3)}\t|{round(abs(a-b),3)}|")
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

    while(abs(f(xi)) > e):
        xi = a - ((b-a)*f(a))/(f(b)-f(a))
        # print(f"i={i} a={round(a, 3)} b={round(b, 3)} x={round(xi, 3)} f(a)={round(f(a),3)} f(b)={round(f(b), 3)} |a-b|={round(abs(a-b),3)}")
        print(f"|{i}\t|{round(a, 3)}\t|{round(b, 3)}\t|{round(xi, 3)}\t|{round(f(a),3)}\t|{round(f(b), 3)}\t|{round(abs(a-b),3)}|")
        if(f(xi)*f(a) > 0): a = xi
        else: b = xi
        i += 1
    print(f"calculation result: root={round(xi, 3)}")

def simple_iteration():

    print("----------- Метод простой итерации ------------")
    a = 0.2953
    b = 3.0585
    e = 0.001

    l = 100
    f = lambda x : 1.62*x**3 - 8.15*x**2 + 4.39*x + 4.29
    phi = lambda x : 162*x**3 - 815*x**2 + 440*x + 429
    i = 0
    xi = b
    x_prev = xi + 2*e

    while(abs(xi - x_prev) > e):
        x_prev = xi
        xi = phi(xi)
        print(f"i={i} x_(i-1)={round(x_prev, 3)} f(xi)={round(f(xi), 3)} xi={round(xi, 3)} phi(x_prev)={round(phi(x_prev),3)} |a-b|={round(abs(xi - x_prev),3)}")
        # print(f"|{i}\t|{round(x_prev, 3)}\t|{round(f(xi), 3)}\t|{round(xi, 3)}\t|{round(phi(x_prev),3)}\t|{round(abs(xi - x_prev),3)}|")
        i += 1
    print(f"calculation result: root={round(xi, 3)}")

# hord_method()
# half_devidion()
simple_iteration()