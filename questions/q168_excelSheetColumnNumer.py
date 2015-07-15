'''
Given a positive integer, return its corresponding
column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
class Solution(object):
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        abcs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "A"*(n/26)+abcs[(n%26)]


if __name__ == '__main__':
    inpnum=43
    print Solution().convertToTitle(inpnum)