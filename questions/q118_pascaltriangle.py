'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows < 1:
            return []
        pasc = [[1], [1, 1]]
        if numRows == 1:
            return pasc[:1]
        numRows -= 2
        while numRows:
            nextpasc = []
            currpasc = pasc[-1]
            for idx in range(len(currpasc)-1):
                nextpasc.append(currpasc[idx]+currpasc[idx+1])
            pasc.append([1]+nextpasc+[1])
            numRows -= 1
        return pasc
