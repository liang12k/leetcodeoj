'''
Given an array of numbers nums, in which exactly two elements appear
only once and all the other elements appear exactly twice.
Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important.
So in the above example, [5, 3] is also correct.
---
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsdict={}
        for n in nums:
            numsdict[n]=numsdict.get(n,0)+1
        nums=[]
        for k,v in numsdict.iteritems():
            if v==1: nums.append(k)
        return nums
    
    def singleNumber_alt(self, nums):
        # reduce
        # apply function of two arguments cumulatively to the items of
        # iterable, from left to right, so as to reduce the iterable
        # to a single value.
        # eg, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
        # calculates ((((1+2)+3)+4)+5)
        #
        # operator.xor
        # Return the bitwise or of a and b.
        #
        # reduce will apply operator.xor on each nums paired
        # iterably from L-to-R
        # operator.xor takes exclusively or of values
        # eg: 10 ^ 11 -> 01
        #     1,1==0, 0,1==1
        #     100 ^ 10 -> 110
        #     1,_==1, 0,1==1, 0,0==0
        #     110 ^ 11 -> 101
        #     1,_==1, 1,1==0, 0,1==1
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor,
                    filter(lambda x: x & xor & -xor, nums))
        return [ans, ans ^ xor]

# 64ms per leetcode

# ref solution that meeds the constant space complexity
# singleNumber_alt
# https://leetcode.com/discuss/52387/3-line-python-code