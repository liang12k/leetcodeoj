def getRangeClosestSqRtToNum(inpNum):
    ''' gets [n-1,n] range surrounding inpNum '''
    for n in xrange(inpNum/2.0):
        if n*n > inpNum:
            return (n-1),n
