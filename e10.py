# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# 
limit = 2000000
sum_of_primes = 0

sieve = [True] * limit
sieve[0] = sieve[1] = False

for index,value in enumerate(sieve):
    if value is True:
        for j in range(index*index, limit, index):
            sieve[j] = False

        sum_of_primes = sum_of_primes + index
        if sum_of_primes == limit:
            break
        else:
            continue

print "Sum of the first %d primes is %d" % (limit, sum_of_primes)
