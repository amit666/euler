"""
    https://projecteuler.net/problem=81
"""
import csv

result_data = {}

data = []
for row in csv.reader(open('p081_matrix.txt')):
    data.append(row)

def min_path(x, y):
    key = "{}:{}".format(x, y)
    if key in result_data:
        return result_data[key]

    result = int(data[x][y])
    if x == 0 and y > 0:
        result += min_path(0, y - 1)
    elif x > 0 and y == 0:
        result += min_path(x - 1, y)
    elif x > 0 and y > 0:
        result += min(min_path(x - 1, y), min_path(x, y - 1))

    result_data[key] = result
    return result

print(min_path(79, 79))
