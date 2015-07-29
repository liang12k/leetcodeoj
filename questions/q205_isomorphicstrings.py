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

Note: You may assume both s and t have the same length.
'''
class Solution(object):
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        # assuming both s,t are same length
        if not s:
            return True
        # values to handle the initial set up of char to num mappings
        # first char has 1, then everything else has idx+1 sequencially
        # the nums str hands the numerical sequence of the char mappings
        # *note*: start @ idx 1 as the dict.get for 0 is False, enters
        #         else statement nonetheless to set at 1
        sidx = 2
        sdict = {s[0]: 1}
        snums = ""
        tidx = 2
        tdict = {t[0]: 1}
        tnums = ""
        for idx in range(len(s)):
            sch = s[idx]
            tch = t[idx]
            # for each char, append to dict and the latest num str
            # increment the respective idx+1 if new char encountered
            # *note*: faster to slice list to get char in the else stmts
            if sdict.get(sch):
                snums += str(sdict[sch])
            else:
                snums += str(sidx)
                sdict[sch] = snums[-1]
                sidx += 1
            if tdict.get(tch):
                tnums += str(tdict[tch])
            else:
                tnums += str(tidx)
                tdict[tch] = tnums[-1]
                tidx += 1
            # check the latest char appended
            # if sequence isn't the same, broken
            if snums[-1] != tnums[-1]:
                return False
        # everything checked and isomorphic
        return True


if __name__ == '__main__':
    print Solution().isIsomorphic("ab", "aa")
