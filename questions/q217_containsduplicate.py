'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''
class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        # base case
        if not nums: return False
        # using dict to check if duplicates exist
        ctrdict={}
        for n in nums:
            # create dict key for 'n' element if it doesn't exist
            ctrdict[n]=ctrdict.get(n,0)+1
            # if duplicate, return True
            if ctrdict[n]>1: return True
        # by default, return False, unique list of elements
        return False