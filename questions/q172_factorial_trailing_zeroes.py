'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # http://mathandmultimedia.com/2014/01/25/zeros-are-there-in-n-factorial/
        # http://www.nerdparadise.com/math/algebra/factorialzeros/
        # keep breaking down num n by pow of 5 by division
        # take the whole int val and cont. until pow of 5 > n, meaning no zeroes left
        trailingZeroes=0
        div=5
        while n/div:
            trailingZeroes+=(n/div)
            div*=5
        return trailingZeroes