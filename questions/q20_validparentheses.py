'''
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''
class Solution(object):
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        # base case
        if not s: return True
        if len(s)%2: return False # odd len isn't valid
        stk=[]
        for ch in s:
            # start keeping track
            if ch in ["(","{","["]:
                stk.append(ch)
            else:
                # if end parenthesis, curly brace, sq bracket
                # and empty stack, invalid str
                if not stk: return False
                if   ch==")" and stk[-1]!="(": return False
                elif ch=="}" and stk[-1]!="{": return False
                elif ch=="]" and stk[-1]!="[": return False
                # by default, valid end char to pop last elem
                stk.pop(-1)
        # if empty, valid str, else there are lingering values
        # *note*:
        # bool(stk) on empty list returns False even for valid str!
        return True if not stk else False