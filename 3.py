'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import math, time
def fhpf(num):
    factors = [i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]
    for i in range(len(factors)):
        factors.append(num / factors[i])
    factors = [factor for factor in factors if isPrime(factor)]
    return max(factors)
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
start = time.time()
print(fhpf(600851475143))
print(time.time() - start)
#Overview-based Solution
def ofhpf(num):
    while num % 2 == 0:
        num /= 2
    factor = 3
    lastFactor = 1
    while num > 1:
        while num % factor == 0:
            num /= factor
            lastFactor = factor
        factor += 2
    return lastFactor
start = time.time()
print(ofhpf(600851475143))
print(time.time() - start)
