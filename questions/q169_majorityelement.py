'''
Given an array of size n, find the majority element.
The majority element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and
the majority element always exist in the array.
'''
class Solution(object):
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        # dict to hold each int's count
        numsd={}
        # get value of half of len to avoid repeat of same value
        numsHalfLen=len(nums)/2
        for n in nums:
            # set in the new occurrence count
            # 'count' variable holds the occurrence value
            # -prevent fetching in dict; ~slow key-value retrieval
            count=numsd[n]=numsd.get(n,0)+1
            if count>numsHalfLen:
                # return value if majority
                return n