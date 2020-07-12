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

# A bit array demo - written for Python 3.0
import array

def makeBitArray(bitSize, fill = 0):
    intSize = bitSize >> 5                   # number of 32 bit integers
    if (bitSize & 31):                      # if bitSize != (32 * n) add
        intSize += 1                        #    a record for stragglers
    if fill == 1:
        fill = 4294967295                                 # all bits set
    else:
        fill = 0                                      # all bits cleared

    bitArray = array.array('I')          # 'I' = unsigned 32-bit integer

    bitArray.extend((fill,) * intSize)

    return(bitArray)

# testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
def testBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return(array_name[record] & mask)

# setBit() returns an integer with the bit at 'bit_num' set to 1.
def setBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] |= mask
    return(array_name[record])

# clearBit() returns an integer with the bit at 'bit_num' cleared.
def clearBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = ~(1 << offset)
    array_name[record] &= mask
    return(array_name[record])

# toggleBit() returns an integer with the bit at 'bit_num' inverted, 0 -> 1 and 1 -> 0.
def toggleBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] ^= mask
    return(array_name[record])

bits = 65_536_00                             # upper limit on primes
ini = 1
myArray = makeBitArray(bits, ini)
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# 0 and 1 are not prime, and not included in the Sieve of Eratosthenes:
bit = 0
clearBit(myArray, bit)
bit = 1
clearBit(myArray, bit)

for index in range(256):            # range is to "square root" of limit
    test = testBit(myArray, index)

    if test:
        zeroBit = index * index     # prime squared is lowest multiple left

        while zeroBit < 65_536_00:
            clearBit(myArray, zeroBit)
            zeroBit += index

for index in range(65_536_00):
    test = testBit(myArray, index)
    if test:
        print(index, end=",")



def pqubes():
    pass

def primes(limit):
    f = [x for x in range(1, limit)]
    f[0] = 0
    x = 1;
    while x<len(f):
        if x >1 and f[x] > 0:
            # print(f[x]-1, end=" ")
            i = x
            while i < len(f)-x:
                i += x
                f[i] = 0


        x += 1

    print(f)

def prime_proof():
    pass

# if __name__ == "__main__":
    # f = 2
    # for x in range(2048):
    #     f = f<<1
    #     print(f)
    # primes(100)
