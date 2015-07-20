'''
Implement pow(x, n).
'''
class Solution(object):
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        answ=1
        while n > 0:
            answ = answ*(x**(n % 2))
            n /= 2
            answ = answ*(x**n)
        return answ


if __name__ == '__main__':
    base = 34.00515
    expon = -3
    print Solution().myPow(base,expon)
    # expecting 0.00003