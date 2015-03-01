#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#

import math

def squareOfSumOfNaturalNumbers(n):
    return sumOfNaturalNumbers(n) * sumOfNaturalNumbers(n)

def sumOfNaturalNumbers(n):
    return n*(n+1)/2

def sumOfSquaresOfNaturalNumber(n):
    return (n * (n+1) * (2 * n + 1)) / 6

N = 100
difference = abs(sumOfSquaresOfNaturalNumber(N) - squareOfSumOfNaturalNumbers(N))
print "Sq (sum) - Sum (Sq) = %d" % (difference)
