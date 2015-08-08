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
        pasc=[[1],[1,1]]
        numRows-=2
        while numRows:
            nextpasc=[1]
            currpasc=pasc[-1]
            idx=0
            while (idx+1)<len(currpasc):
                nextpasc.append(currpasc[idx]+currpasc[idx+1])
                idx+=1
            nextpasc.append(1)
            pasc.append(nextpasc)
            numRows-=1
        return pasc[-1]
