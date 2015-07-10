'''
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if not s: return True
        s=list(s)
        for idx,z in enumerate(s):
            if not z.isalnum(): s[idx]=""
            else: s[idx]=z.lower()
        s="".join(s)
        return s==s[::-1]