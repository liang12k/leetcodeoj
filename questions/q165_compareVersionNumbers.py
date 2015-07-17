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
        version1=[int(v) for v in version1.split(".")]+[0]
        version2=[int(v) for v in version2.split(".")]+[0]
        if version1[0]>version2[0]:
            return 1
        elif version2[0]>version1[0]:
            return -1
        else:
            if version1[1]>version2[1]:
                return 1
            elif version2[1]>version1[1]:
                return -1
            return 0


if __name__ == '__main__':
    inp1="10.6.5"
    inp2="10.6"
    print Solution().compareVersion(inp1,inp2)
    # expecting 1, returning 0