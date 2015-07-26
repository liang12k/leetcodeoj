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

pattern is:
1  :  1
2  :  11
3  :  21
4  :  1211
5  :  111221
6  :  312211
7  :  13112221
8  :  1113213211
9  :  31131211131221
'''
class Solution(object):
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        # base case
        if n == 1:
            return "1"
        # initial str
        sstr = "1"
        # keep expanding num str for n iterations
        # *note*: n==1 handled at base case
        while n > 1:
            # ans holds the latest num str at n-iteration
            # need to reset for every iteration to get latest
            # -see end of while-loop; take ans if while-loop ends
            ans = ""
            # curr num to keep count @
            curr = sstr[0]
            # initial counter
            ctr = 0
            # iterate thru each num str element
            for num in sstr:
                num = str(num)
                if num == curr:
                    ctr += 1
                else:
                    # set ans to latest
                    # *note*: going from left to right, append as such
                    ans += str(ctr)+curr
                    # set curr to latest num, reset ctr
                    curr = num
                    ctr = 1
            # exiting for-loop; still remains the latest curr & its ctr
            # append it accordinglt to ans
            # *note* if end of while-loop, take ans and return
            ans += str(ctr)+curr
            # set ans as latest sstr for next iteration if needed
            sstr = ans
            # decrement n for while-loop
            n -= 1
        return ans


if __name__ == '__main__':
    for n in range(1, 10):
        print n, " : ", Solution().countAndSay(n)
