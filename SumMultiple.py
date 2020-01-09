
def SumMultiple(x):
    newSum = 0
    for eachNum in range(x):
        if eachNum % 3 == 0 or eachNum % 5 == 0:
            newSum += eachNum
    print(newSum)

SumMultiple(1000)

