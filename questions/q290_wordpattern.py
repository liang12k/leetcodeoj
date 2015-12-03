'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution(object):
    def wordPattern(self, pattern, strr):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=strr.split(" ")
        if len(pattern)!=len(s): return False # base case
        # 2 dicts, each to remember the patternChar->subStr, subStr->patternChar
        pdict={}
        sdict={}
        for idx,text in enumerate(s):
            if text in sdict and sdict[text]!=pattern[idx]:
                return False # check if text in sdict, if so, does its patternChar match?
            if pattern[idx] in pdict and pdict[pattern[idx]]!=text:
                return False # check if patternChar in pdict, if so, does its text match?
            # add into respective dicts for mapping
            sdict[text]=pattern[idx]
            pdict[pattern[idx]]=text
        return True