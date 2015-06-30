''''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
(ask yourself what are the possible input cases.)

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the
first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical digits
as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral
number, or if no such sequence exists because either str is empty or it contains
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''
class Solution(object):
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if not str: return 0
        isalphanum,isneg=False,False
        num=""
        for s in str:
            if s:
                if s in ["-","+"] and signchanged not in [False,True]:
                    isneg = s=="-"
                    signchanged=True
                    continue
                if s.isdigit():
                    num+=s
                    continue
                isalphanum=True
                break
        if isalphanum: return 0
        num=int(num)
        if isneg:
            num=0-num
        if num>2147483647 or num<-2147483648:
            num=0
        return num


if __name__ == '__main__':
    Solution().myAtoi("    010") # expected 0, returned -2