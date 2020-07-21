# A bit array demo - written for Python 3.0
import array
import math


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

def demo(limit):
    # bits = 65_536 # upper limit on primes
    bits = limit # upper limit on primes
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

if __name__ == "__main__":
    demo()
