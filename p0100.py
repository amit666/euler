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

prev, blue, disks, ratio = 4, 15, 5, Decimal(5.828427124746189846860033867415)
increments = 0
count = 0
corr_exp = 4
multiplier = 1
correction = 16
search_started_at = 0


def signal_handler(sig, frame):
    print()
    print_status()
    sys.exit(0)


def print_status():
    c_needed = int(correction - increments)
    if c_needed < 0:
        c_needed = 0
    print(
        "{:8.1f}s [{:2}{:40,}|{:<40,}][10^{:<5.0f}] correction(appl,needed):{:20,}|{:<20,} ratio:{:30.30f} inc:{:12,} blue_inc:{:12,}".format(
            default_timer() - start, count, disks,
            blue, math.log10(disks), int(correction), c_needed, ratio, increments, blue_inc_count))


signal.signal(signal.SIGINT, signal_handler)

wait_count = 0
blue_inc_count = 0
blue_proc_time = 0

max_f = 0

while True:
    if disks % 1000_000 == 0:
        wait_count += 1
        time_since_last = default_timer() - last_print
        if time_since_last > 10 + wait_count:
            print("Evaluating(time since last:{:<10,} blue_proc:{:<10,}... delta:{:<40,}  actual:{:<40,}  starting-point:{:<40,}".format(
                int(time_since_last), blue_proc_time, disks - search_started_at, disks, search_started_at))
            last_print = default_timer()
            blue_proc_time = 0

    start_blue = default_timer()
    large = 0
    blue_delta = disks * (disks - 1) - 2 * blue * (blue - 1)
    if blue_delta > 1000:
        # print("blue delta > 10000, blue:", blue)
        blue = int(disks / math.sqrt(2))

    while disks * (disks - 1) > 2 * blue * (blue - 1):
        # print("blue delta <= 10000, blue:", blue)
        large += 1
        if large> max_f:
            print("f:", large)
            max_f = large
        blue_inc_count += 1
        blue += 1
    blue_proc_time += default_timer() - start_blue

    if disks * (disks - 1) == 2 * blue * (blue - 1):
        print_status()
        wait_count = blue_inc_count = blue_proc_time = increments = 0

        last_print = default_timer()
        if count < 20:
            correction *= 1.01
        elif count < 280:
            correction *= 5
        else:
            print("20x multiplier")
            correction *= 20
            print("Correction:{:40,}".format(int(correction)))

        # correction = int(correction)
        count += 1

        # if count < 20:
        # ratio = disks / prev
        prev = disks

        # disks, blue = [int(ratio * x) - int(correction) for x in [prev, blue]]
        disks = int(ratio * prev) - int(correction)
        blue = int(disks / math.sqrt(2))
        if blue > 1000:
            blue -= 1000

        search_started_at = disks


    disks += 1
    increments += 1
