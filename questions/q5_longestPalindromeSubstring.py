'''
# https://goo.gl/CO0QoR

Chomolungma - Dynamic Programming solution:

Basic thought is simple. when you increase s by 1 character, you could only
increase maxPalindromeLen by 1 or 2, and that new maxPalindrome includes this
new character. Proof: if on adding 1 character, maxPalindromeLen increased by
3 or more, say the new maxPalindromeLen is Q, and the old maxPalindromeLen
is P, and Q>=P+3. Then it would mean, even without this new character, there
would be a palindromic substring ending in the last character, whose length
is at least Q-2. Since Q-2 would be >P, this contradicts the condition that
P is the maxPalindromeLen without the additional character.

So, it becomes simple, you only need to scan from beginning to the end,
adding one character at a time, keeping track of maxPalindromeLen, and
for each added character, you check if the substrings ending with this new
character, with length P+1 or P+2, are palindromes, and update accordingly.

Now, this is O(n^2) as taking substrings and checking palindromicity
seem O(n) time. We can speed up it by realizing that strings are immutable,
and there are memory slicing tricks will help to speed these operations up.
comparing string equality with "==" is O(1), and using slicing to substring
and reverse is O(n) < O(_n_) < O(n^2) (thanks to ChuntaoLu).
But as slicing is optimized by the interpreter's C code, it should run
pretty fast.


ChuntaoLu explanation on runtime O(n) < O(_n_) < O(N^2)

Great DP solution, it runs much faster than the 'traverse and grow both ways'
O(n^2) solution, and the reason is exactly that checking string equality
with '==' is amortized O(1). I am no Python guru, but I am pretty sure slicing
and reversing is O(k) where k is the sliced/reversed string length, because
those operations create new string objects and involves copying characters.
So, technically it is not O(n), but it is about 5 times faster than the
O(n^2) solution I mentioned.
'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0: return 0
        maxLen,start=1,0
        for i in xrange(1,len(s)):
            # note: the endrange is always 'i+1', one idx after current 'i' idx
            #       cmp the (i - _n_) prior elems 
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                # continue iteration because this is a longer string
                # no need to check its interior elems as this is valid already
                continue
            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        # return the palindrome substring of max length
        return s[start:start+maxLen]


if __name__=="__main__":
    ss="aaabaaaa"
    print Solution().longestPalindrome(ss)