'''
Write a function that takes an unsigned integer and
returns the number of '1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation
00000000000000000000000000001011,
so the function should return 3.
'''
class Solution(object):
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return sum([int(_) for _ in "{0:032b}".format(n, "b")])

# 72ms per leetcode
