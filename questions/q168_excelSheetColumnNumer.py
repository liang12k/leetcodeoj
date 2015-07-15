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
        ans=""
        while (n>0):
            ans+=abcs[(n-1)%26]
            n/=26
        return ans[::-1]


if __name__ == '__main__':
    inpnum=26
    # expecting 'AZ', getting 'Z'
    print Solution().convertToTitle(inpnum)