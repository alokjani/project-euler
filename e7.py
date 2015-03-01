#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#

limit = 1000000
count = 0
prime_found = 2

sieve = [True] * limit      # list of Primality flags
sieve[0] = sieve[1] = False

for index,value in enumerate(sieve):
    if value is True:
        for j in range(index*index, limit, index):
            sieve[j] = False

        count = count + 1
        prime_found = index
        
        if count == 10001:
            break

    else:
        continue

print "The %d th prime found is %d" % (count, prime_found)
