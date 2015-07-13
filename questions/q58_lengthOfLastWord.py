'''
Given a string s consists of upper/lower-case alphabets
and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of
non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''
class Solution(object):
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if not s: return 0
        lenctr=0
        metwhsp=False
        slen=len(s)
        for idx in range(slen-1,-1,-1):
            if s[idx]!=" ": lenctr+=1
            else:
                if not metwhsp: metwhsp=True
                if metwhsp and lenctr: return lenctr
        return lenctr


if __name__ == '__main__':
    inp=" a"
    print Solution().lengthOfLastWord(inp)