'''
Write a function to find the longest common prefix string
amongst an array of strings.
'''
class Solution(object):
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        # base cases
        if not strs: return ""
        if len(strs)==1: return strs[0]
        lcp=strs[0] # take first element
        for s in strs[1:]:
            # empty string is a common prefix for all
            if lcp=="" or s=="": return ""
            # begin @ 0 for all str cmp ('a'[:0] returns '')
            idx=0
            # continue until non matching char
            while lcp[:idx]==s[:idx]:
                idx+=1
                # exit if idx is beyond either lens to avoid indexerror
                if idx>len(lcp) or idx>len(s): break
            # this is current longest common prefix w latest idx
            lcp=s[:idx-1]
        return lcp


if __name__ == '__main__':
    inp=["a","b"]
    print Solution().longestCommonPrefix(inp)