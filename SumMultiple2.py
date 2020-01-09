def SumMultiple2(x):
    x1 = int((x-1)/3)
    x2 = int((x-1)/5)
    x3 = int((x-1)/15)
    
    sumNum = 3*0.5*x1*(x1+1)+5*0.5*x2*(x2+1)-15*0.5*x3*(x3+1)

    print(sumNum)
SumMultiple2(1000)

