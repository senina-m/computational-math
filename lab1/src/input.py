
import re
from sys import stdin

# TODO: think about errors
def read_from_stdin():
    
    print("Type coefficient matrix with colums devided by whitspace and rows by \"\\n\"")
    matrix = []
    # n = 0
    for line in stdin:
        if line == '':
            break
        data = line.strip().split(" ")
        data = [float(i) for i in data]
        # if matrix == []:
        #     n = len(data)
        matrix.append(data)
        #TODO: finish readin after ns line

    return matrix

def read_from_file(filename):
    f = open(filename, "r")
    matrix = []
    data = f.readline().strip().split(" ")
    data = [float(i) for i in data]

    for line in range (len(data) - 2):
        matrix.append(data)
        data = f.readline().strip().split(" ")
        data = [float(i) for i in data]
    matrix.append(data)
    return matrix