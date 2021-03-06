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
        # sort both input strings by char
        # determine if the sorted lists are the same
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t

# total runtime on leetcode is 96ms
