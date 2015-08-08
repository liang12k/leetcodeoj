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
        # base of pascal triangle for numRows in [1,2]
        pasc = [[1], [1, 1]]
        # use pasc as is for 0,1,2
        # *note*: pasc[:0] == []
        if numRows < 2:
            return pasc[:numRows]
        # begin getting pascal values from numRows>2
        numRows -= 2
        while numRows:
            nextpasc = []
            currpasc = pasc[-1]
            # iterate thru latest pascal value list
            # end when the idx+1 goes beyond the len range
            for idx in range(len(currpasc)-1):
                nextpasc.append(currpasc[idx]+currpasc[idx+1])
            # all pascal values begin,end with 1
            # append generated pascal value into pasc list
            pasc.append([1]+nextpasc+[1])
            numRows -= 1
        return pasc
