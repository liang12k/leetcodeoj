'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be
replaced to get t.

All occurrences of a character must be replaced with another
character while preserving the order of characters.
No two characters may map to the same character but a character
may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''
class Solution(object):
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if not s: return True
        sidx = 1
        sd = {s[0]:0}
        snums = ""
        tidx = 1
        td = {t[0]:0}
        tnums = ""
        for idx in range(len(s)):
            sch = s[idx]
            tch = t[idx]
            if sd.get(sch):
                snums += str(sd[sch])
            else:
                snums += str(sidx)
                sd[sch] = snums[-1]
                sidx += 1
            if td.get(tch):
                tnums += str(td[tch])
            else:
                tnums += str(tidx)
                td[tch] = tnums[-1]
                tidx += 1
            if snums[-1] != tnums[-1]:
                return False
        return True


if __name__ == '__main__':
    print Solution().isIsomorphic("ab", "aa")
