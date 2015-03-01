# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isEvenlyDivisibleInRange(start,end,num):
    for i in range(start,end):
        if num % i != 0:
            return False

    return True


i = 100
while (True):
    print "testing %d" % (i)
    if isEvenlyDivisibleInRange(1,20,i):
        print i
        break

    i = i + 1
    # must be divisible by 2, 10
    while ( i % 17 != 0 or i % 19 != 0 or i % 13 !=0 ):
        i = i + 1

