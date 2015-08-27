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

# 64ms per leetcode
