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
        # split all whitespaces
        # *note*: these values in list are now ''
        s=s.split(" ")
        for elem in s[::-1]:
            # reverse the str list; start from end
            # for the first non whitespace str, return len of str
            if elem!="": return len(elem)
        # default entire str is whitespaces
        return 0


if __name__ == '__main__':
    inp="a "
    print Solution().lengthOfLastWord(inp)