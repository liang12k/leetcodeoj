'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if -1<rowIndex<4: return [[1],[1,1],[1,2,1],[1,3,3,1]][rowIndex]
        pascalTriNums=[1,3,3,1] # from here, begins @ [1,3,3,1]
        rowIndex-=3
        while rowIndex:
            pascalTriNums=[1]+[pascalTriNums[x]+pascalTriNums[x+1] for x in xrange(len(pascalTriNums)-1)]+[1]
            rowIndex-=1
        return pascalTriNums