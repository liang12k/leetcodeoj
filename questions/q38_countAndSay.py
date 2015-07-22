'''
The count-and-say sequence is the sequence of integers
beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''
class Solution(object):
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        n = str(n)
        ans = ""
        idx = 1
        currn = n[0]
        currlen = 1
        while idx < len(n):
            if n[idx] == currn:
                currlen += 1
            else:
                ans = ans+str(currlen)+currn
                currn = n[idx]
                currlen = 1
            idx += 1
        ans = ans+str(currlen)+currn
        return ans


if __name__ == '__main__':
    print Solution().countAndSay(1)
    # expecting '1', returning '11'
