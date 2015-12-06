'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this is fib question
        # but the initial starting numbers are 1,1
        # because w 1 stair, min of 1 possibility of 1 step
        #
        # 1, 1, 2, 3, 5, 8, 13, 21, ...
        # w 3 stair-steps, there are 2 possibilities
        # w 6 '' '' '' '', '' '' ''  8 '' ''
        a=1
        b=1
        while n:
            a,b=b,a+b # fib swap
            n-=1
        return a # return current