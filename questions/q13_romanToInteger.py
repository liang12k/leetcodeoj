'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        numstr=0
        rmnums=[
            (1000, 'M'), (900, 'CM'), (500, 'D'),  (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        while s:
            for pair in rmnums:
                n,r=pair
                lenr=len(r)
                if s[:lenr]==r:
                    numstr+=n
                    s=s[lenr:]
        return numstr