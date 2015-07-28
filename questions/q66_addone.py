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
        # base case: at least 1 (if input is 0)
        totalsum = 1
        # reversed() returns a generator
        for idx, elem in enumerate(reversed(digits)):
            # get total sum using modulus
            # use idx as the exponent at 10th place
            totalsum += (elem*(10**idx))
        # reuse the digits variable
        digits = []
        while totalsum > 0:
            # insert is faster than list concating
            digits.insert(0, totalsum % 10)
            totalsum /= 10
        return digits
