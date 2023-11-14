import random

def generatePoints(c,d):
    x = []
    y = []
    for i in range(c):
        x.append(random.uniform(1,d))
        y.append(random.uniform(1,d))
        #print(x[i], y[i])
    return x, y

def calcCorrel(x,y):
    num = 0
    xDen = 0
    yDen = 0
    xMean = 0
    yMean = 0
    
    for i in range(len(x)):
        xMean = xMean + x[i]
        yMean = yMean + y[i]
    xMean = xMean/len(x)
    yMean = yMean/len(y)
    #print(xMean)
    #print(yMean)
    for i in range(len(x)):
        num = num + (x[i]-xMean) * (y[i]-yMean)
        xDen = xDen + (x[i]-xMean)**2
        yDen = yDen + (y[i]-yMean)**2
    return num/((xDen*yDen)**(1/2))

total = 0
numOfTrials = 1000
numOfPoints = 1000
pointRange = 10000
a=0
temp = 0
for i in range(numOfTrials):
    x = []
    y = []
    x,y = generatePoints(numOfPoints,pointRange)
    temp = calcCorrel(x,y)
    total = total + temp
    if temp > 0.1 or temp < -0.1:
        a = a + 1
print(total/numOfTrials)
print(a)
    
