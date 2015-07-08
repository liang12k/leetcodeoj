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
            while lcp[:idx]==s[:idx]:
                idx+=1
                if idx>len(lcp) or idx>len(s): break
            lcp=s[:idx-1]
        return lcp


if __name__ == '__main__':
    inp=["a","b"]
    print Solution().longestCommonPrefix(inp)