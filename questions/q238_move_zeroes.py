'''
Given an array nums, write a function to move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # **note**: in-place means the .append, .extend, .remove, .pop ... etc list-methods
        idx=0
        numsLen=len(nums)
        while numsLen:
            if nums[idx]==0:
                nums.pop(idx) # pop idx that's 0 value
                nums.append(0) # add in-memory to the end
                # go back 1 idx to check
                # if @ idx 0, go to -1 (end of list) and continue fwd, new idx 0 value, and onward...
                idx-=1
            numsLen-=1 # decrement as we're iterating thru list, avoid hitting the newly appended 0's @ tail
            idx+=1 # proceed to next idx