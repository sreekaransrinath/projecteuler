'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
#Bruteforce
from time import time
def findLargestPalindrome(high):
    return max([item for sublist in [[i * j for j in range(high + 1) if str(i * j) == str(i * j)[::-1]] for i in range(high * 9 // 10, high + 1)] for item in sublist])
def pldr(high):
    largest = 0
    for i in range(high, high * 9 // 10):
        for j in range(high, i):
            if str(i * j) == str(i * j)[::-1]:
                if i * j < largest:
                    return largest
                largest = i * j
    return largest
start = time()
print(findLargestPalindrome(999))
print(time() - start)
start = time()
print(findLargestPalindrome(999))
print(time() - start)

# def findLargestPalindrome():
#     for i in range((999 * 999), 1, -1):
#         # print(i)
#         if str(i) == str(i)[::-1]:
#             print(i, )

# print(findLargestPalindrome())