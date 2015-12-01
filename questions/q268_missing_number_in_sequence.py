'''
Given an array containing n distinct numbers taken
from 0, 1, 2, ..., n, find the one that is missing
from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the sum of all nums sequentially from 1...n is
        # (n * (n+1)) / 2
        # therefore, taking len of nums, you get it's len 'n'
        # however, the sum of that differs from
        # sum of nums itself
        # getting a diff of the expected sequence sum
        # against the actual sequence sum (w len of n-1, the missing number)
        # missing num is returned
        #
        # **note**
        #   this problem has sequences starting at 0
        #   (n * (n+1)) / 2 is for a sequence starting at 1
        #   getting a diff will determine if 0 is missing at start
        #
        # eg:
        #   [0,1,3]
        #   expected sum based on len 3: [1,2,3] == 6
        #   actual list sum: [0,1,3] == 4
        #   missing num: 2
        #
        #   [1,2,3,4]
        #   expected sum based on len 4: [1,2,3,4] == 10
        #   actual list sum: [1,2,3,4] == 10
        #   missing num: 0 <-- the starting number
        #
        len_nums=len(nums)
        return ((len_nums * (len_nums+1))/2) - sum(nums)