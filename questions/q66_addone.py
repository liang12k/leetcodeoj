'''
Given a non-negative number represented as an array of digits,
plus one to the number.

The digits are stored such that the most significant digit is
at the head of the list.
'''
class Solution(object):
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        totalsum = 1
        for idx, elem in enumerate(reversed(digits)):
            totalsum += (elem*(10**idx))
        digits = []
        while totalsum > 0:
            digits.insert(0, totalsum % 10)
            totalsum /= 10
        return digits
