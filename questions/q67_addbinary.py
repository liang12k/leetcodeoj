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
        # idea is to reverse both str a,b
        # get the sum of both as int values
        # using the idx of each elem as the expon for 2**idx
        # then determine the binary str of the sum
        # in the while loop using %2 result
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
        # save space, replace 'b'
        b = ""
        while intsum > 0:
            b = str(intsum % 2)+b
            intsum /= 2
        return b
