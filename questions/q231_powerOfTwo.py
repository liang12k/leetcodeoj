'''
Given an integer, write a function to determine
if it is a power of two.
'''
# rework needed, too slow
# idea: check for binary '1' position and the rest are 0

class Solution(object):
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        # base case, no exponent reaches 0 or negative nums
        if n <= 0:
            return False
        # keep decrementing 'n'
        # *note*: this also handles n==1
        #         won't enter the while loop, goes straight to return
        while n > 1:
            # a remainder means it's odd
            if n % 2:
                return False
            # decrement
            n /= 2
        return True
