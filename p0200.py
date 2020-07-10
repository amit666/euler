"""
    https://projecteuler.net/problem=200

Find the 200th prime-proof sqube containing the contiguous sub-string "200"

Problem 200
We shall define a sqube to be a number of the form, p2q3, where p and q are distinct primes.
For example, 200 = 5223 or 120072949 = 232613.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call
such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200".
"""

from timeit import default_timer

start = default_timer()


def rd(x, width=0):
    return "{:,}".format(x).ljust(width)


def loop():
    blue_disks = 0
    total_disks = 2
    prev_total_disks = 0

    f_total_disks = total_disks * (total_disks - 1)
    f_blue_disks = blue_disks * (blue_disks - 1)

    while True:
        while f_total_disks > 2 * f_blue_disks:
            blue_disks += 1
            f_blue_disks = blue_disks * (blue_disks - 1)

        if f_total_disks == 2 * f_blue_disks:
            execution_time = default_timer() - start
            print(execution_time, "seconds; #disks:", rd(total_disks, 22), "; #blue:", rd(blue_disks, 13))
            if prev_total_disks:
                ratio = total_disks / prev_total_disks
                prev_total_disks = total_disks

                total_disks = int(ratio * total_disks)
                f_total_disks = total_disks * (total_disks - 1)

                blue_disks = int(ratio * blue_disks)
                f_blue_disks = blue_disks * (blue_disks - 1)
                continue
            else:
                prev_total_disks = total_disks

        total_disks += 1
        f_total_disks = total_disks * (total_disks - 1)


if __name__ == "__main__":
    loop()
