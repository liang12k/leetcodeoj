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
        # base case, blank str right at beginning
        if not needle:
            return 0
        # use to slice haystack list
        needleLen = len(needle)
        # idx counter to keep track where needle may first occur
        idx = 0
        # keep going until len unable to be used for cmp
        while len(haystack) >= needleLen:
            # return idx of first needle occurrence
            if needle == haystack[:needleLen]:
                return idx
            # increment idx counter
            idx += 1
            # slice haystack list forward
            haystack = haystack[1:]
        return -1
