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
        # base case
        if not s: return True
        # convert to list to replace any non alphanum char w ''
        s=list(s)
        for idx,z in enumerate(s):
            # eplace any non alphanum char w ''
            if not z.isalnum(): s[idx]=""
            # lowercase all valid chars
            else: s[idx]=z.lower()
        # rejoin list to sing str
        s="".join(s)
        return s==s[::-1]