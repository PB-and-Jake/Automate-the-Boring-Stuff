#chapter 4 practice- COMMA CODE

def commas(someList):
    returnStr = ''
    for i in range(len(someList)):
        if i==len(someList)-1:
            returnStr+='and '+str(someList[i])
        else:
            returnStr+=(str(someList[i])+', ')
    return returnStr

print(commas([1,2,3,4,5,6,7]))
print(commas(['Johnson', 'Juan', 'Johnny', 'John']))
