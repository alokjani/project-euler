# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(num):
    return int(str(num)[::-1])

def isPalindrome(num):
    if num == reverse(num):
        return True
    return False

smallest_3_digit_num = 100
largest_3_digit_num  = 999

largest_palindrome = 0
for i in range(smallest_3_digit_num,largest_3_digit_num):
    for j in range(smallest_3_digit_num, largest_3_digit_num):
        num = i * j
        if isPalindrome(num):
            if num > largest_palindrome:
                largest_palindrome = num
            print "%d x %d = %d" % (i,j,largest_palindrome)

print "largest palindrome that is a product of two 3 digit numbers is %d" % (largest_palindrome)


