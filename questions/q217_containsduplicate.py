'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''
class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums: return False
        ctrdict={}
        for n in nums:
            ctrdict[n]=ctrdict.get(n,0)+1
            if ctrdict[n]>1:
                return True
        return False