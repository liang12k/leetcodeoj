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
        # the counter of the str length
        lenctr=0
        # bool to determine if whitespace met
        metwhsp=False
        # keep len value to avoid refetching
        slen=len(s)
        # start from end of str 's'
        for idx in range(slen-1,-1,-1):
            # if char, increment
            if s[idx]!=" ": lenctr+=1
            else:
                # indicate whitespace met
                if not metwhsp: metwhsp=True
                # case when many whitespace at end of str
                # then a set of char(s) appear
                # eg: 'a     '
                if metwhsp and lenctr: return lenctr
        return lenctr


if __name__ == '__main__':
    inp=" a"
    print Solution().lengthOfLastWord(inp)