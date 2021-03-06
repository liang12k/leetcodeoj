'''
Given a sorted array and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numsLen=len(nums)
        startidx=0
        endidx=numsLen-1
        # approach: binary search
        #           close the start,end idx range
        while endidx!=startidx:
            midpt=(endidx+startidx)/2
            if target<=nums[midpt]:
                endidx=midpt
            else:
                # if target > nums[midpt], skip this midpt, begin at next
                startidx=midpt+1
        # determine if idx should be this idx or the one after
        # since this new num can be a duplicate value
        return startidx if target<=nums[startidx] else startidx+1