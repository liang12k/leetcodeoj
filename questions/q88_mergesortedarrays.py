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
        ## the idea is m, n are the range of [0:_z_]
        ## where _z_ is for nums1 (m idx), nums2 (n idx)
        n1=nums1[:m]
        n2=nums2[:n]
        # slice, and extend
        n1.extend(n2)
        n1.sort()
        # this creates an entire copy of nums1
        # assign the new n1 to it
        nums1[:]=n1
        
        ## shorter pythonic 2 liner
        ## http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
        ## modify a copy of nums1 at idx [m:]
        # seeing as nums1 idx range is [0:m]
        # don't care abt the rest, so overwrite it
        # with nums2[:n] values then sort in memory
        # nums1[m:]=nums2[:n]
        # nums1.sort()