'''
Given two strings s and t, write a function to determine if
t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s = sorted(list(s))
        t = sorted(list(t))
        for pair in zip(s, t):
            if pair[0] != pair[1]:
                return False
        return True
