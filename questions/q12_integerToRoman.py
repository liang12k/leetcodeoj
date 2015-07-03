'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        romanstr=""
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
            # continue decrementing num with current n value from rmnums list
            # exit and go to next until num has finished decrementing
            while num-n>-1:
                romanstr+=r # concat roman numeral str
                num-=n      # decrement num using current n
        return romanstr