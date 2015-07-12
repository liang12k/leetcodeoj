class Solution(object):
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if not s: return True
        if len(s)%2: return False
        stk=[]
        for ch in s:
            if ch in ["(","{","["]:
                stk.append(ch)
            else:
                if not stk:
                    return False
                if ch==")" and stk[-1]!="(":
                    return False
                elif ch=="}" and stk[-1]!="{":
                    return False
                elif ch=="]" and stk[-1]!="[":
                    return False
                stk.pop(-1)
        return True if not stk else False