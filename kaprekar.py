"""
    https://projecteuler.net/problem=100

Arranged probability
Problem 100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two
discs were taken at random, it can be seen that the probability of taking two blue discs,
        P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box
containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the
number of blue discs that the box would contain.
"""

import math
import signal
import sys
from decimal import Decimal
from timeit import default_timer

start = last_print = default_timer()

def num_2_list(x):
    list = []
    while x > 0:
        list.append(x % 10)
        x //= 10
    list.reverse()
    return list


def list_2_num(list):
    if not list:
        return 0
    return list[0] * int(math.pow(10, len(list) - 1)) + list_2_num(list[1:])

for original in range(1000, 10_02):
    for x in range(10):
        list = num_2_list(original)
        list.sort()
        low = list_2_num(list)
        list.reverse()
        high = list_2_num(list)
        diff = high - low
        # print("original:", original, "high:", high, "low:", low, "diff:", diff)
        original = diff
    print(original)


