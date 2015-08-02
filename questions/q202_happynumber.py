'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
'''
class Solution(object):
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        # n needs to be a positive int
        if n < 1:
            return False
        # n add to the array of met numbers
        metnums = [n]
        # initial var to hold total sum
        # list comprehension to convert n to str the get int of each
        totalsum = sum([(int(d) % 10)**2 for d in str(n)])
        # while loop until totalSum==1 or a bool returned
        # such as number already met (looping cycle)
        while totalsum != 1:
            if totalsum in metnums:
                return False
            metnums.append(totalsum)
            # set n to latest totalsum
            n = totalsum
            # recalculate totalsum
            totalsum = sum([(int(d) % 10)**2 for d in str(n)])
        return True


if __name__ == '__main__':
    print Solution().isHappy(3)
