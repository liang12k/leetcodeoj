'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot=nums[0] # using quickselect; https://en.wikipedia.org/wiki/Quickselect
        leftList=[]
        equalList=[]
        rightList=[]
        for n in nums: # unsorted nums list, need to contain the vals
            if n>pivot:
                rightList+=[n]
            elif n==pivot:
                equalList+=[n]
            else:
                leftList+=[n]
        # determine if length of right,equal,left vs k using recursion
        # if kth falls into the len of rightList side, the elem is here
        if k<=len(rightList):
            return self.findKthLargest(rightList,k)
        elif (k-len(rightList))<=len(equalList):
            return equalList[0] # decr the idxs against k b/c rightList side vals are ignored
        else:
            return self.findKthLargest(leftList,k-len(rightList)-len(equalList)) # investig into leftList side