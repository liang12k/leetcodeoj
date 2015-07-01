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
        if x==0: return True
        x=str(x)
        for idx,n in enumerate(x):
            if x[idx]!=x[0-idx-1]: break
        if x[0]=="-": return False
        x=int(x)
        if x>=2147483647 or x<=-2147483648:
            x=0
        return bool(x)


if __name__ == '__main__':
    print Solution().isPalindrome(10) # expected False, returning True (because of bool(x))