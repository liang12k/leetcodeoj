'''
Given a non-negative integer num, repeatedly add all its digits
until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
class Solution(object):
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        # exit while loop once reached single digits [0:9] inclusive
        while num > 9:
            # get sum as we go along num until exit
            num = sum([int(_) for _ in str(num)])
        return num

    def addDigits_alternate(self, num):
        # https://leetcode.com/discuss/52144/ac-neat-python-solution
        # operate on base-9 [0:9] inclusive
        # 68ms
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        # alternate one-liner
        # evaluate in order
        # (num and 9) to ensure num==0 returns 0 too as (0 and 9) is False
        # return num%9 or num and 9

# 72ms per leetcode
