import matplotlib.pyplot as plt

def plot_result(x, y, f, method):
    fig = plt.figure()
    fig.suptitle('differentiation result', fontsize=20)
    ax = fig.add_subplot(111)
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.plot(x, y, marker="o", label=f"{method} differentiation result") #marker circle
    plt.plot(x, f, marker=".", label="input function") #marker point
    for i,j in zip(x, [round(i, 3) for i in y]):
        ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
        ax.annotate('(%s,' %i, xy=(i,j))
    plt.legend()
    plt.show()
    pass

def plot_both_results(f, x, y_milan, y_runge, f_result):
    fig = plt.figure()
    fig.suptitle('differentiation result', fontsize=20)
    ax = fig.add_subplot(111)
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.plot(x, y_runge, marker="o", color="green", label=f"runge-kutta differentiation result") #marker circle
    plt.plot(x, y_milan, marker="o", color="red", label=f"milan differentiation result") #marker circle
    plt.plot(x, f_result, marker=".", color="blue", label="input function") #marker point
    ax.grid()
    #для того, чтобы подписывать значения на графике
    # for i,j in zip([round(i, 3) for i in x], [round(i, 3) for i in f_result]):
    #     ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
    #     ax.annotate('(%s,' %i, xy=(i,j))
    # for i,j in zip([round(i, 3) for i in x], [round(i, 3) for i in y_runge]):
    #     ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
    #     ax.annotate('(%s,' %i, xy=(i,j))
    plt.legend()
    plt.show()