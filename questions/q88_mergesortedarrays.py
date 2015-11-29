'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space
(size that is greater or equal to m + n) to
hold additional elements from nums2.
The number of elements initialized in nums1 and nums2
are m and n respectively.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        n1=nums1[:m]
        n2=nums2[:n]
        n1.extend(n2)
        n1.sort()
        nums1[:]=n1
        
        ## http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
        ## modify a copy of nums1 at idx [m:]
        # nums1[m:]=nums2[:n]
        # nums1.sort()