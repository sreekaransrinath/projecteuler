'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import math, time
lim = 10001
primes = [n for n in range(1, lim + 1) if for i in range(2, int(math.sqrt(n) + 1) n % i == 0)]
print(primes)