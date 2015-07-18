'''
Given a string, find the length of the longest substring
without repeating characters.
For example, the longest substring without repeating letters for
"abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution(object):
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        maxlen = 0
        longestStr = ""
        for ch in s:
            if ch not in longestStr:
                # keep appending onto the current longest str
                # if it's an original char
                longestStr += ch
            else:
                # if repeated char detected, continue the new substring
                # from the index+1 of the original char
                longestStr = longestStr[longestStr.index(ch)+1:] + ch
            maxlen = max(maxlen, len(longestStr))
        return maxlen
