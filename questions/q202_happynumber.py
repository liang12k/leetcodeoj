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
        if n<0: return False
        metnums=[n]
        sum=0
        # need to handle sum==1 after entire n's digits done
        # being squared
        # the while condition will immediately break if sum==1
        # during the summing of n's digits!
        while sum!=1:
            sum+=(n%10)**2
            n/=10
            print "sum: ",sum
            print "n: ",n
            if n==0:
                if sum==1:
                    return True
                if sum in metnums:
                    return False
                metnums.append(sum)
                n=sum
                sum=0
                print "n==0"
                print "metnumd: ", metnums
                print "n: ", n
        return True


if __name__ == '__main__':
    print Solution().isHappy(3)
    # expecting False
