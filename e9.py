total = 1000
for a in range(3,1000):
    for b in range(a+1,1000):
        c = total - a - b
        if a*a + b*b == c*c:
            print "Pythagorean triplet %d %d %d has sum %d" % (a,b,c,a+b+c)

