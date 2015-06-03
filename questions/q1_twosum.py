"""
Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        # targetDiffsList holds the diffs of the vals until found target diff
        # when target diff found, get the index within targetDiffsList for elem
        # return the [minIdx,maxIdx] vals
        # else keep appended diffs until the end
        targetDiffsList=[]
        for idx,n in enumerate(nums):
            if n in targetDiffsList:
                return sorted([idx+1,targetDiffsList.index(n)+1])
            targetDiffsList.append(target-n)