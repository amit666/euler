"""
    https://projecteuler.net/problem=100

Arranged probability
Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box
containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of
blue discs that the box would contain.
"""
import math
import signal
import sys
from timeit import default_timer

start = default_timer()

prev, blue, disks, ratio = 4, 15, 5, 5
increments = 0
count = 0
corr_exp = 4
multiplier = 1
correction = 1

def signal_handler(sig, frame):
    print()
    print_status()
    sys.exit(0)


def print_status():
    print("{:8.1f}s [{:2}{:40,}|{:<40,}][10^{:<5.0f}] correction:{:<20,} ratio:{:20.20f}, inc:{:12,}".format(default_timer() - start, count, disks,
                                                                                 blue, math.log10(disks), int(correction), ratio, increments))


signal.signal(signal.SIGINT, signal_handler)


while True:
    while disks * (disks - 1) > 2 * blue * (blue - 1):
        blue += 1

    if disks * (disks - 1) == 2 * blue * (blue - 1):
        correction *= 1.7
        print_status()
        count += 1
        ratio = disks / prev
        prev = disks
        disks, blue = [int(ratio * x - correction) for x in [disks, blue]]
        increments = 0

    disks += 1
    increments += 1
