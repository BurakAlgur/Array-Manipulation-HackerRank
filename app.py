def arrayManipulation(n, inputArr):

    newArr = n*[0]
    for i in inputArr:
        indexRange = range(i[0],i[1] +1)
        for j in indexRange:
            newArr[j-1] += i[2]
    
    return max(newArr)
        
        
inputArr = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]
n = 5

print(arrayManipulation(n,inputArr))






