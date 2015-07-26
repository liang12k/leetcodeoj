'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        intsum = 0
        a = a[::-1]
        for idx, num in enumerate(a):
            if num == "1":
                intsum += (2**idx)
        b = b[::-1]
        for idx, num in enumerate(b):
            if num == "1":
                intsum += (2**idx)
        if not intsum:
            return "0"
        b = ""  # save space, replace 'b'
        while intsum > 0:
            b = str(intsum%2)+b
            intsum /= 2
        return b