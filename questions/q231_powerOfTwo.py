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
    '''
    # same runtime as above, 80ms according to leetcode
    def isPowerOfTwo_alt(self, n):
        if n <= 0:
            return False
        # using str format to get binary format of number
        n = "{0:b}".format(n).count("1")
        # if only one occurrence of '1' in binary format str,
        # it's a power of 2 (eg: 32==10000, 8==100)
        if n == 1:
            return True
        return False
    '''
