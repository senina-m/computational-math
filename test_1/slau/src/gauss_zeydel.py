from gauss import print_matrix, swap_lines


def gauss_zeydel(matrix, e):
    print("------------gauss_zeydel iteration--------------")

    # матрица должна быть записана в виде
    # x_0 = a_1*x_1 + a_*2*x_2 + c_0
    # x_1 = a_0*x_0 + a_*2*x_2 + c_1
    # x_2 = a_0*x_0 + a_*1*x_1 + c_2

    print_matrix("matrix", matrix)

    n = len(matrix)
    x = [0]*(n)
    for i in range(n):
        if(matrix[i][i] == 0):
            matrix = swap_lines(matrix, i) # тут нужен другой своп -- чтобы было преобладание диагональных элементов
        a = matrix[i][i]
        for j in range(n + 1):
            matrix[i][j] /= a
        matrix[i][i] = 1
    x_prev = [matrix[i][-1] for i in range(n)]
    print_matrix("get ready", matrix)


    # печать верная если СЛАУ из 3х уравнений
    print(f"k\tx0\tx1\tx2\tdiff")
    print(f"0\t{round(x_prev[0], 3)}\t{round(x_prev[1], 3)}\t{round(x_prev[2], 3)}\t-")

    k = 1
    while True:
        for i in range(n):
            print(f"x[{i}] =")
            a = 0
            for j in range(n):
                if j > i:
                    a += -matrix[i][j]*x_prev[j]
                    print(f"+ {round(-matrix[i][j], 3)}*{round(x_prev[j], 3)}")
                elif j < i:
                    a += -matrix[i][j]*x[j]
                    print(f"+ {round(-matrix[i][j], 3)}*{round(x[j], 3)}")
            x[i] = a + matrix[i][-1]
            print(f"+ {matrix[i][-1]} = {round(x[i], 3)}")

        diff = max([abs(x_prev[i] - x[i]) for i in range(n)])
        print(f"{k}\t{round(x[0], 3)}\t{round(x[1], 3)}\t{round(x[2], 3)}\t{round(diff, 3)}")

        if diff < e:
            break
        else:
            x_prev = x
            k += 1
    
    print("------------gauss_zeydel iteration end--------------")
    return x

