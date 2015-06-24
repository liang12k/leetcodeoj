## solution is ~ @ 160ms, needs to be faster
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        # note: the direction is |/|/|/...|/|
        # return str s as is for base cases
        if numRows==1 or numRows>=len(s): return s
        initrow=0
        endcol=True
        d={}
        # iterate O(n) thru str s
        for ch in s:
            # append ch into proper row
            d[initrow]=d.get(initrow,[])+[ch]
            # increment initrow if on 0 or (coln-1)%nRows==0
            # as this means the chars go downward
            # decrement initrow if not on 0 or (coln-1)%nRows==0
            # as these are the diagonals
            initrow=initrow+(1 if endcol else -1)
            if initrow==numRows:
                # after finish incrementing over rows
                # go back to the diagonal position for decrementing
                # eg: ABCD, 3
                # 0 A
                # 1 B D <-- 'D' went over and is in the diagonal
                # 2 C
                initrow-=2
                endcol=False
            elif initrow==-1:
                # after finish decrementing over diagonal
                # go back to the 0 row position for incrementing
                # eg: ABCDE, 3
                # 0 A   E <-- 'E' went over and is in the new row 0, col0
                # 1 B D
                # 2 C
                initrow+=2
                endcol=True
        # concat all list values of chars for return output
        s=""
        for _ in xrange(numRows):
            s+="".join(d.get(_,""))
        return s