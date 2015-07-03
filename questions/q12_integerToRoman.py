'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        romanstr=""
        rmnums=[
            (1000, 'M'), (900, 'CM'), (500, 'D'),  (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        for pair in rmnums:
            n,r=pair
            while num-n>-1:
                romanstr+=r
                num-=n
        return romanstr