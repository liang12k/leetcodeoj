'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
if version1 < version2 return -1,
otherwise return 0.

You may assume that the version strings are non-empty and
contain only digits and the . character.
The . character does not represent a decimal point and
is used to separate number sequences.
For instance, 2.5 is not "two and a half" or
"half way to version three", it is the
fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 10.6 < 10.6.5 < 13.37
'''
class Solution(object):
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        # split string by '.' to get individual nums
        version1=[int(v) for v in version1.split(".")]
        version2=[int(v) for v in version2.split(".")]
        # make both version nums lists equal in len
        # place in filler 0s if needed
        if len(version1)>len(version2):
            version2+=[0]*(len(version1)-len(version2))
        elif len(version2)>len(version1):
            version1+=[0]*(len(version2)-len(version1))
        while version1 and version2:
            # begin at 0 index to cmp
            idx=0
            if version1[idx]>version2[idx]: return 1
            elif version2[idx]>version1[idx]: return -1
            # increment idx by 1 to get the next and remaining values
            # *note*: [2][1:] returns []
            idx+=1
            version1=version1[idx:]
            version2=version2[idx:]
        # all else, the version numbers are the same
        return 0


if __name__ == '__main__':
    inp1="1.0"
    inp2="1"
    print Solution().compareVersion(inp1,inp2)