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


if __name__ == '__main__':
    base = 34.00515
    expon = -3
    print Solution().myPow(base, expon)
