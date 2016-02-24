'''
Given an integer, write a function to determine if
it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''
from math import log


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ## # is this a valid approach? using a while-loop
        if n<1:
            # avoid neg nums, and 0 isn't do able
            return False
        # include 1, as 3**0 == 1
        while n>0:
            if n%3!=0 and n!=1:
                # check each modulos, exclude valid 3**0
                return False
            # keep breaking n it down
            n /= 3
        # default n is a power of 3 after finish breaking down
        return True
    
    def isPowerOfThree_alt(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # handle base case n can't be powered to 0
        # this uses the log approach to get the cube of n
        # needs to handle different precision as
        # the log will be a float against a rounded down log
        return n>0 and abs(log(n,3) - round(log(n,3))) < 1e-10
    