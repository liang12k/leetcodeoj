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
# ref: https://leetcode.com/discuss/19139/python-solution-with-explanation
class Solution(object):
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        # str of capitalized letters
        abcs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        # keep going until n is depleted
        while (n>0):
            # *note*: to be in %26 range, need to stay in 0-25
            # appending the letter at head since math is handling
            # the str from right to left
            ans=abcs[(n-1)%26]+ans
            # decrement by (n-1) to stay in %26 range
            n=(n-1)/26
        return ans


if __name__ == '__main__':
    inpnum=26
    print Solution().convertToTitle(inpnum)