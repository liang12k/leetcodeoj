'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

If the integer's last digit is 0, what should the output be?
ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow?
Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows.
How should you handle such cases?

For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows.
'''
# ref: http://www.programcreek.com/2012/12/leetcode-reverse-integer/
class Solution(object):
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        # **need to catch overflow on int value!**
        # 
        # requires modulus, division operations
        # shifting numbers & tracking if neg. number (if so, 0-reversednum)
        # modules takes the tail digit,
        # - make this the leading digit
        # - sum to the latest result * 10 (shifting it)
        # keep dividing to get the next
        # ** repeat until digit is taken
        negflag=False
        if x<0:
            negflag=True
            x=0-x # make number positive
        res=0
        while(x>0):
            mod=x%10
            x=x/10
            res=res*10+mod
        if negflag:
            res=0-res # if originally negative, flip back to negative
        # detect overflow
        # sys.maxint    ==  2147483647 (max)
        # -sys.maxint-1 == -2147483648 (min)
        if res>2147483647 or res<-2147483648:
            res=0
        return res