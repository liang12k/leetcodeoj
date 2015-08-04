'''
Reverse bits of a given 32 bits unsigned integer.

For example:
given input 43261596
(represented in binary as 00000010100101000001111010011100),
return 964176192
(represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''
class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int("{:08b}".format(n)[::-1], 2)


if __name__ == '__main__':
    print Solution().reverseBits(1)
    '''
    input 1 (00000000000000000000000000000001)
    expecting
    output 2147483648 (10000000000000000000000000000000)
    '''
