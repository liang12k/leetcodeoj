'''
The count-and-say sequence is the sequence of integers
beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

---
https://leetcode.com/discuss/40007/if-i-input-2-the-expected-integer-is-11-%EF%BC%9F

The task says - generate the sequence.
the sequence is made the way when item N is build based on N-1
so item 1 - always 1 as a start point.
the next item you build pairs based on the previous item
following the riles rules ...

and here is how the sequence is built (added . and : to separate pairs)

1 -> 1 (start point)
2 -> 1.1 (based on previous element which is 1)
3 -> 2.1 (where it says we have 2 count of digit 1)
4 -> 1.2:1.1 (where it says we have 1 count of digit 2
              and 1 count of digit 1)
5 -> 1.1:1.2:2.1 (1 count of 1, 1 count of 2, 2 count of 1)
etc.
'''
class Solution(object):
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        # idea: start answ='1'
        #       use logic below to get nth idx element
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
