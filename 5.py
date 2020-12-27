'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import math, time
high = 20
start = time.time()
# Check for primes
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
# Find all primes in given range
primes = [n for n in range(1, high + 1) if isPrime(n)]
# Find highest power of each of those primes
def findHighestPwr(n):
    if n == 1:
        return 1
    rng = list(range(high + 1))
    lastPwr = 1
    while 1:
        if n ** (lastPwr) not in rng:
            return n ** (lastPwr - 1)
        lastPwr += 1 
# Multiply the highest powers of each prime
print(math.prod([findHighestPwr(n) for n in primes]))
print(time.time() - start)