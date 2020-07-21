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
from bitarray import *

start = default_timer()

def set qubes():
    pass

def primes(limit):
    # bits = 65_536 # upper limit on primes
    bits = limit  # upper limit on primes
    ini = 1
    myArray = makeBitArray(bits, ini)
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # 0 and 1 are not prime, and not included in the Sieve of Eratosthenes:
    bit = 0
    clearBit(myArray, bit)
    bit = 1
    clearBit(myArray, bit)

    for index in range(int(math.sqrt(limit))):
        if testBit(myArray, index):
            zeroBit = index * index  # prime squared is lowest multiple left

            while zeroBit < bits:
                clearBit(myArray, zeroBit)
                zeroBit += index

    count = 0
    for index in range(bits):
        if testBit(myArray, index):
            count += 1
            if count % 20 == 0:
                print()
            print("{:,}".format(index), end=" ")


def prime_proof():
    pass

if __name__ == "__main__":
    primes(1000000)
