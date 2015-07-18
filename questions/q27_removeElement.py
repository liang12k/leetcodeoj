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
        # idea to start from end of list
        # handle each and move towards 0 index
        numslen = len(nums)-1
        while numslen > -1:
            if nums[numslen] == val:
                # pop the desired value out of list
                # .pop handles the edit in place
                nums.pop(numslen)
            # decrement to next index
            numslen -= 1
        return len(nums)
