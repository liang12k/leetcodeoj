'''
Given a column title as appear in an Excel sheet,
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
class Solution(object):
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        d={'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3, 'G': 6, 'F': 5, 'I': 8, 'H': 7, 'K': 10, 'J': 9, 'M': 12, 'L': 11, 'O': 14, 'N': 13, 'Q': 16, 'P': 15, 'S': 18, 'R': 17, 'U': 20, 'T': 19, 'W': 22, 'V': 21, 'Y': 24, 'X': 23, 'Z': 25}
        # reverse str 's', begin from 0 index
        s=s[::-1]
        num=0
        # loop thru reversed str 's' from 0 index
        # iteratively, each index is 26**index
        # multiplied by respective alphabet numerical value +1
        # ^ as excel column numbers start @ A==1
        # eg: 'DBA' --> 'ABD' :
        #     A = (0+1)*26**0 # idx 0
        #     B = (1+1)*26**1 # idx 1
        #     D = (3+1)*26**2 # idx 2
        for idx,ch in enumerate(s):
            num=(1+d.get(ch))*26**idx+num
        return num


if __name__ == '__main__':
    inp="DBA"
    print Solution().titleToNumber(inp)