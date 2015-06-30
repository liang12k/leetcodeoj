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
        isneg=False
        # determine if sign is changed or not
        # None is a neutral value
        signchanged=None
        num=""
        for s in str:
            if s!=" ":
                # case when it's a valid sign change
                if s in ["-","+"] and signchanged not in [False,True]:
                    isneg = s=="-" # use bool value returned
                    signchanged=True
                    continue
                # add to current num str
                if s.isdigit():
                    num+=s; continue
                # detect a char or invalid signchange, leave at latest num
                break
            # handle cases like '   + 123', '  +0 321', '   +-1'
            # where sign is changed already too
            if num or signchanged in [False,True]: break
        # if blank, return as is
        if not num: return 0
        num=int(num)
        # bring it back to negative
        if isneg: num=0-num
        # leave num at max,min range if outlying beyond int range
        if num>=2147483647: num=2147483647
        elif num<=-2147483648: num=-2147483648
        return num


if __name__ == '__main__':
    print Solution().myAtoi("   - 321")