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