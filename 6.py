'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
num = 100
def sumofSquares(num):
    return sum([n ** 2 for n in range(num + 1)])
def squareofSum(num):
    return sum([n for n in range(num + 1)]) ** 2
print(squareofSum(num) - sumofSquares(num))

#Overview Implementation
def diff(num):
    return ((num * (num + 1) / 2) ** 2)- ()