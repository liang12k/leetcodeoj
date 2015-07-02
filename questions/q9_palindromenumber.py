'''
Determine whether an integer is a palindrome. Do this without extra space.

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string,
note the restriction of using extra space.

You could also try reversing an integer.
However, if you have solved the problem "Reverse Integer", you know that the
reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''
class Solution(object):
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        x=str(x)
        # iterate thru entire str of nums
        for idx in xrange(len(x)):
            # check from front and back values towards center
            # this handles detecting the '-' sign as neg nums aren't palindromes
            if x[idx]!=x[0-idx-1]: return False
        # as all values meet palindrome requirement
        # bool if x doesn't surpass int max value for overflow
        return not int(x)>=2147483647