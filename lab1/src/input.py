
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
    data = re.split(" \t", f.readline().strip())
    data = [float(i) for i in data]
    while (data != []):
        matrix.append(data)
        data = re.split(" \t", f.readline().strip())

    return matrix