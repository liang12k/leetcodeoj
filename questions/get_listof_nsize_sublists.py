def getListOfNSizeSublists(inputList, nSize):
    ''' get a list of sublists of n-size base on inputlist elements '''
    answ=[]
    while inputList:
        # pythonic approach to slice and append
        answ.append(inpList[:nSize])
        # slice the list from idx nSize to break down the list
        inpList=inputList[nSize:]
    return answ