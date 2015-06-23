class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        # note: the direction is |/|/|/...|/|
        # 
        # ideas:
        # O(n) go thru whole 's' in single pass
        # need to handle base case of few chars (w applying the logic below)
        # numRows for number of lists to hold values
        # idx to keep vals within list
        # idx to keep count where char is entered
        # 
        # whitespaces, TBD (are they needed?)
        # -'ignore' them and just add in the char at correct positions
        def convert(self, s, numRows):
            if numRows==1 or numRows>len(s): return s
            rowslist=range(numRows)
            d={}
            for idx,ch in enumerate(s):
                coln=0
                if idx%numRows==0 and idx!=0:
                    coln+=1
                if coln not in [0,numRows-1]:
                    d[rowslist[0-(idx%numRows)-2]]=d.get(rowslist[0-(idx%numRows)-2],[])+[ch]
                else:
                    d[idx%numRows]=d.get(idx%numRows,[])+[ch]
            s=""
            for _ in xrange(numRows):
                s+="".join([ch for ch in d.get(_,"") if ch])
            return s


if __name__=="__main__":
    print Solution().convert("ABCDE",3)
    # giving "ABDEC", should be "AEBDC" (passed 219/1158)
    # error somewhere in inserting chars