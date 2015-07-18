'''
Given an array and a value, remove all instances
of that value in place and return the new length.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        numslen = len(nums)-1
        while numslen > -1:
            if nums[numslen] == val:
                nums.pop(numslen)
            numslen -= 1
        return len(nums)
