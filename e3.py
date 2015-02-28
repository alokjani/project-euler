# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt 
num = 600851475143

def isPrime(num):
    return all(num % i for i in xrange(2,num))

def isFactor(num,divisor):
    if num % divisor is 0:
        return True
    return False

factor = 0
for i in xrange(2, int(sqrt(num)) ):
    if isFactor(num,i):
        if isPrime(i):
            factor = i
            print factor

print "largest prime factor found %d" % (factor)
