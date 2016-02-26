'''
Given an array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/discuss/62111/one-line-python-solution-with-o-n-time
        # https://leetcode.com/discuss/6170/my-o-n-solution-using-xor
        return reduce(lambda x,y: x^y, nums)

'''

reduce will take the first 2 elements of the iterable
then the next +1 onwards, 'collapsing' the iterable

[1,2,3,4,5] --> ((((1+2) +3 ) +4) +5)

XOR (exclusive OR)
initally, it'll start with 0 then
specifically looks for only 1 occurrence of the element
if there is more than one of the element, it'll return 0
else returns the number (meaning there's only one of it)

'''