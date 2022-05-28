import matplotlib.pyplot as plt

# def show_input_data(x, y):
#     fig = plt.figure()
#     fig.suptitle('input data', fontsize=20)
#     plt.xlabel('x', fontsize=16)
#     plt.ylabel('y', fontsize=16)
#     fig.savefig('interpolation_input_data.png')
#     plt.plot(x, y, label="input data")
#     plt.legend()
#     plt.show()

def plot_result(f, x, y, method):
    # fig = plt.figure()
    # fig.suptitle('differentiation result', fontsize=20)
    # ax = fig.add_subplot(111)
    # plt.xlabel('x', fontsize=16)
    # plt.ylabel('y', fontsize=16)
    # plt.plot(x, y, marker="o", label=f"{method} differentiation result") #marker circle
    # fx  = [f(x[i], y[i]) for i in range(len(x))]
    # plt.plot(x, fx, marker=".", label="input function") #marker point
    # for i,j in zip(x, [round(i, 3) for i in y]):
    #     ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
    #     ax.annotate('(%s,' %i, xy=(i,j))
    # plt.legend()
    # plt.show()
    pass

def plot_both_results(f, x, y_milan, y_runge):
    fig = plt.figure()
    fig.suptitle('differentiation result', fontsize=20)
    ax = fig.add_subplot(111)
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.plot(x, y_runge, marker="o", label=f"runge-kutta differentiation result") #marker circle
    plt.plot(x, y_milan, marker="o", label=f"milan differentiation result") #marker circle
    fx  = [f(x[i], y_milan[i]) for i in range(len(x))]
    plt.plot(x, fx, marker=".", label="input function") #marker point
    for i,j in zip([round(i, 3) for i in x], [round(i, 3) for i in y_milan]):
        ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
        ax.annotate('(%s,' %i, xy=(i,j))
    for i,j in zip([round(i, 3) for i in x], [round(i, 3) for i in y_runge]):
        ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
        ax.annotate('(%s,' %i, xy=(i,j))
    plt.legend()
    plt.show()