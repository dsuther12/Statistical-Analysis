import math
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

input_string = input("Enter elements of a list seperated by a space: ")
dataList = input_string.split()

for i in range(len(dataList)):
    dataList[i] = int(dataList[i])


df = pd.DataFrame(dataList)

mpl.use('agg')

fig = plt.figure(1, figsize=(9, 6))
#plt.xticks([0], ["Data Set"])
ax = fig.add_subplot(111)
bp = ax.boxplot(dataList)
plt.xticks([1], ["Entered Data Set"])


def meanCalc(dataList):
    num = 0

    for i in range(len(dataList)):
        num = dataList[i] + num

    return num / len(dataList)


def standardDev(dataList, meanCalc):

    standDevList = []
    num = 0

    for i in range(len(dataList)):

        num = (dataList[i] - meanCalc(dataList)) ** 2
        standDevList.append(num)
        num = 0


    return math.sqrt(meanCalc(standDevList))

def numMin(dataList):
    dataList.sort()

    return dataList[0]

def numMax(dataList):
    dataList.sort()

    return dataList[len(dataList) - 1]

def numMedian(dataList):
    dataList.sort()

    median = 0

    if(len(dataList) % 2 == 0):
        median = (dataList[int((len(dataList) - 1) / 2)] + dataList[int(((len(dataList) - 1) / 2)) + 1]) / 2
        return median
    else:
        median = dataList[int((len(dataList) - 1) / 2)]
        return median

def numQ1(dataList):

    if((len(dataList) - 1) % 2 == 0):
        midNum = int(len(dataList) / 2)
        q1 = dataList[:midNum]
        medQ1 = (q1[int((len(q1) - 1) / 2)] + q1[int(((len(q1) - 1) / 2)) + 1]) / 2
        #print(q1)
        return medQ1
    else:
        midNum = int(len(dataList) / 2)
        q1 = dataList[:midNum]
        medQ1 = q1[int((len(q1) - 1) / 2)]
        #print(q1)
        return medQ1

def numQ3(dataList):

    if((len(dataList) + 1) % 2 == 0):
        midNum = int(len(dataList) / 2) + 1
        q3 = dataList[midNum:]
        medQ3 = (q3[int((len(q3) - 1) / 2)] + q3[int(((len(q3) - 1) / 2)) + 1]) / 2
        #print(q3)
        return medQ3
    else:
        midNum = int(len(dataList) / 2)
        q3 = dataList[midNum:]
        medQ3 = q3[int((len(q3) - 1) / 2)]
        #print(q3)
        return medQ3

def outliers(dataList):
     IQR = numQ3(dataList) - numQ1(dataList)
     bigOutlierList = []
     smallOutlierList = []

     for i in range(len(dataList)):

        if dataList[i] > numQ3(dataList) + 1.5 * IQR:
            bigOutlierList.append(dataList[i])
        if dataList[i] < numQ1(dataList) - 1.5 * IQR:
            smallOutlierList.append(dataList[i])

     print("Too small outliers: " + str(smallOutlierList)[1:-1])
     print("Too big outlier: " + str(bigOutlierList)[1:-1])





def fiveNumSum():
    print("Mean: " + str(meanCalc(dataList)))
    print("Standard Deviation: " + str(standardDev(dataList, meanCalc)))
    print("Minimum: " + str(numMin(dataList)))
    print("Maximum: " + str(numMax(dataList)))
    print("Median: " + str(numMedian(dataList)))
    print("Q1: " + str(numQ1(dataList)))
    print("Q3: " + str(numQ3(dataList)))
    print("IQR: " + str(numQ3(dataList) - numQ1(dataList)))
    outliers(dataList)


fiveNumSum()

fig.savefig('fig1.png', bbox_inches='tight')







