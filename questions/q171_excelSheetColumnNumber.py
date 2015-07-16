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
        if not s: return 0
        d={'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3, 'G': 6, 'F': 5, 'I': 8, 'H': 7, 'K': 10, 'J': 9, 'M': 12, 'L': 11, 'O': 14, 'N': 13, 'Q': 16, 'P': 15, 'S': 18, 'R': 17, 'U': 20, 'T': 19, 'W': 22, 'V': 21, 'Y': 24, 'X': 23, 'Z': 25}
        s=s[::-1]
        num=1
        for idx,ch in enumerate(s):
            num=(idx*26)+d.get(ch)+num
        return num


if __name__ == '__main__':
    inp="BA"
    print Solution().titleToNumber(inp)
    # expecting 53, returning 28