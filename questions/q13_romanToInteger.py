'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        numstr=0
        # tuple of standard int and their respective roman numeral str
        # -using tuple as this is fixed & runs faster
        # important to handle the special numbers before a new roman numeral
        # the leading 9, 4 numbers - eg: 900 (CM), 40 (XL)
        # order from larges to least to decrement num from top down (left to right)
        rmnums=(
            (1000, 'M'), (900, 'CM'), (500, 'D'),  (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        )
        for pair in rmnums:
            n,r=pair
            lenr=len(r)
            # keep going for 'chained' roman numeral strs
            while s[:lenr]==r:
                numstr+=n   # sum latest total with new int values
                s=s[lenr:]  # slice str to start at next char
        return numstr