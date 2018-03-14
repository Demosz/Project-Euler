# 10. Finding the sum of all primes below 2,000,000.

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"""
We can iterate by two, because even numbers after 2 cannot be prime.

We can also check for multiples of primes we have already listed, to eliminate calculations on those numbers as well.

Prime number candidates can be represented by the formula 6k +/- 1. I need to figure out why this works before I feel 
comfortable using it, though. 
"""
import math

def isPrime(possible, known):
    for i in known:
        if possible % i == 0:
            return False
    for i in range(2, int(math.sqrt(possible)) + 1):
        if possible % i == 0:
            return False
    return True

def primes_group(N):
    primes = [2, 3]
    count = 1
    while (6 * count) - 1 < N:
        if isPrime((6 * count - 1), primes) and (6 * count - 1) < N:
            primes.append(6 * count - 1)
        if isPrime((6 * count + 1), primes) and (6 * count + 1) < N:
            primes.append(6 * count + 1)
        count += 1
    return primes

def sum(array):
    count = 0
    for i in array:
        count += i
    return count

print sum(primes_group(2000000))
