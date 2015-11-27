'''
Given an integer array nums, find the sum of the elements between indices i and j (i ² j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.numstuple=[0] # initial 0; handles the inclusive idx j
        for n in nums:
            # take the latest tail of numstuple, pyramid sum w latest num and append onto numstuple
            self.numstuple += [self.numstuple[-1]+n]
        self.numstuple=tuple(self.numstuple) # tuple as this is now fixed

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # j is inclusive
        # get diff, as this is a pyramid sum, num @ idx [j+1] > num @ idx [i]
        return self.numstuple[j+1] - self.numstuple[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)