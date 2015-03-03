# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# 
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 

total = 1000
for a in range(3,1000):
    for b in range(a+1,1000):
        c = total - a - b
        if a*a + b*b == c*c:
            print "Pythagorean triplet %d %d %d has sum %d" % (a,b,c,a+b+c)

