'''
Write an efficient algorithm that searches for a
value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the
last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        investigRow=matrix[0] # initial row (handles single row matrix)
        for idx,row in enumerate(matrix):
            if target==row[0]:
                investigRow=row; break # target row found
            elif target<row[0]:
                investigRow=matrix[idx-1]; break # take prev row b/c row[0] is greater (rows-cols are sorted)
            investigRow=row # default take curr row going fwd, not knowing if a row w target exists
        startidx=0
        endidx=len(investigRow)-1
        while startidx!=endidx: # binary search, break down this target row
            midpt=(startidx+endidx)/2
            if target==investigRow[midpt]:
                return True # found target
            elif target>investigRow[midpt]:
                startidx=midpt+1 # ign this midpt, take next idx, close from L
            else:
                endidx=midpt # close from the R
        return target==investigRow[startidx] # entire target row finished, get the bool