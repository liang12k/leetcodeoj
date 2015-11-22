'''
Given a sorted array of integers, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
(^ hint: binary search)

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Subscribe to see which companies asked this question
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[-1,-1]
        left=0
        right=len(nums)-1
        # approach is to close the range using binary approach
        while left<right:
            midptIdx=(left+right)/2
            if nums[midptIdx]>target:
                # if midpt value >, ignore it and move to the L of it for the latest right idx
                right=midptIdx-1
            elif nums[midptIdx]<target:
                # if midpt value <, ignore it and move to the R of it for the latest left idx
                left=midptIdx+1
            else:
                # can take this idx, closing in the range to determine the left idx
                right=midptIdx
        # exiting the while-loop, a start idx (left) should be found, else return default [-1,-1]
        if nums[left]!=target: return ans
        ans[0]=left
        right=len(nums)-1
        while left<right:
            # midptIdx=(left+right+1)/2 always moves the midpt to the right,
            # otherwise, this can be repeated as the left idx won't move,
            # resulting in right idx not moving
            # need to move left idx to the R to close idx-range
            midptIdx=(left+right+1)/2
            if nums[midptIdx]==target:
                left=midptIdx
            else:
                # close the end range closer to the left idx, moving L
                right=midptIdx-1
        ans[1]=left
        return ans