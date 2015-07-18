'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''
class Solution(object):
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle: return 0
        needleLen=len(needle)
        idx=0
        while len(haystack)>=needleLen:
            if needle==haystack[:needleLen]: return idx
            idx+=1
            haystack=haystack[1:]
        return -1