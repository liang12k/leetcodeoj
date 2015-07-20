'''
Implement pow(x, n).
'''
class Solution(object):
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        # flag to determine if n is negative
        # will need to do 1/x**n later if so
        isneg = False
        if n < 0:
            # make n positive for decrementing
            n = 0-n
            isneg = True
        # base is always 1; to the 0th power
        answ = 1
        while n > 0:
            # first modulus
            answ = answ*(x**(n % 2))
            # then decrement by dividing by 2
            n /= 2
            answ = answ*(x**n)
        # if n was originally negative, need to flip into 1/answ
        if isneg:
            answ = 1/answ
        return answ

'''
e.g.:
x=2, n=5 :: (2**5)

5%2==1 -> 2**1 == 2
5/2==2 -> 2**2 == 4
 |
 | use this '2' value
 V
2%2==0 -> 2**0 == 1
2/2==1 -> 2**1 == 2
 |
 | use this '1' value
 V
1%2==1 -> 2**1 == 2
1/2==0 -> 2**0 == 1

n has reached '0' by dividing by 2
therefore
2 * 4 * 1 * 2 * 2 * 1 == 32
'''

if __name__ == '__main__':
    base = 34.00515
    expon = -3
    print Solution().myPow(base, expon)
