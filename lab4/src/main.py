import sys

from input_data import read_data
from approximation.exp import exp_approximation
from approximation.line import line_approximation
from approximation.log import log_appproximation
from approximation.power import power_approximation
from approximation.square import square_approximation
from plot import plot_results

def print_results(results):
    for key in results:
        print(f'{key}={results[key]}')

def print_best(results):
    min = float('inf')
    best = None
    for key in results:
        if(min > results[key]['standart_deviation']):
            min = results[key]['standart_deviation']
            best = key
        print(f"standart_deviation({key})=", (results[key])['standart_deviation'])
    print(f"Best method is {best} with standart_deviation {results[best]['standart_deviation']}")
    for key in results[best].keys:
        print(f"{key}={results[best][key]}")

def check_results_not_none(results):
    for key in results:
        if results[key] == None:
            results.pop(key)

def main():
    data = read_data()
    points = data['dots']

    results = {}
    results['exp'] = exp_approximation(points)
    results['line'] = line_approximation(points)
    results['log'] = log_appproximation(points)
    results['power'] = power_approximation(points)
    results['square'] = square_approximation(points)

    check_results_not_none(results)

    print_results(results)

    plot_results(data, results)

    print_best(results)

    sys.exit(0)

main()