'''
Write a function to find the longest common prefix string
amongst an array of strings.
'''
class Solution(object):
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs)==1: return strs[0]
        lcp=strs[0]
        for s in strs[1:]:
            if lcp=="" or s=="": return ""
            idx=0
            print "before while - lcp: %s; s: %s"%(lcp,s)
            while lcp[:idx]==s[:idx]:
                idx+=1
            lcp=s[:idx]
            print "after while - idx: %d; lcp: %s; s: %s"%(idx,lcp,s)
        return lcp


if __name__ == '__main__':
    inp=["a","b"]
    print Solution().longestCommonPrefix(inp)
    # expecting "", getting "b"