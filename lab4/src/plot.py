from matplotlib import markers, pyplot as plt

def plot_results(data, results):
        x = [point[0] for point in data]
        y = [point[1] for point in data]
        plt.plot(x, y, label="input_data")
        for key in results:
                plt.plot(x, results[key], label=f"{results[key]['string_function']}")
        plt.legend()
        plt.show(block=False)
