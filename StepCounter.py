
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
import statistics


'''
Python scripts for finding steps,
some assumptions:
    1)The structure of the data is going to be zero acceleration 
    followed by the step data
    2)The step data is continuous, not break or no interruption  
'''


#gets the data
def getData(fileName):
    data = pd.read_csv(fileName)
    StepData = []
    for d in range(len(data['x'])):
        magnitudeData = (data['x'][d])**2 + (data['y'][d])**2 + (data['z'][d])**2
        StepData.append(math.sqrt(magnitudeData))
    return StepData


#finds the starting and stopping positions
def StartingandStopingPointFinder(SmoothedArray):
    slopChanges = []
    count = 0
    
    while count < len(SmoothedArray):  
        slopChanges.append(statistics.stdev(SmoothedArray[count:count+5]))
        count = count + 5
        
    standerDv = np.array(slopChanges)
    meanOfArray = standerDv.mean()
    
    NonZeros = [0,0]
    zeros = [0,0]
    startingPointFound = False
    endingPointFound = False
    starting = 0
    ending = 0
    
    for num in range(len(slopChanges)):
        if slopChanges[num]<2:          
            if zeros[0] == 2:
                NonZeros[0] = 0
                NonZeros[1] = 0 
            if zeros[1] == 0:    
                zeros[1] = num
            zeros[0] = zeros[0] + 1
            
        elif slopChanges[num]>2:          
            if NonZeros[0] == 2:
                zeros[0] = 0
                zeros[1] = 0
            if NonZeros[1] == 0:
                NonZeros[1] = num
            NonZeros[0] = NonZeros[0] + 1
            
        if NonZeros[0]>20 and startingPointFound == False:
            starting = NonZeros[1]
            startingPointFound = True

        if zeros[0] > 3 and ((((standerDv[num:]).mean())/meanOfArray) < .70) and startingPointFound == True:
            ending = zeros[1]
            endingPointFound = True
            
        if endingPointFound == True:
            break
       
    return SmoothedArray[starting*5:ending*5], slopChanges


#positive slop is 1 and negative slop is -1
def getSlop(inputArray):
    array_ = []
    for t in range(len(inputArray)):
        if (inputArray[t] - inputArray[t-1] > 0):
            array_.append(1)
        else:
            array_.append(-1)
    return array_


#Counts the steps
def CountTheOnes(inputArray):
    CountOfOnes = 0
    iterationPlace = 0
    consecutiveOnes  = 0
    
    while iterationPlace < len(inputArray):
        if inputArray[iterationPlace] == 1:
            consecutiveOnes = consecutiveOnes + 1
            iterationPlace = iterationPlace + 1
        elif inputArray[iterationPlace] == -1:
            if consecutiveOnes >= 6:
                CountOfOnes = CountOfOnes + 1
            consecutiveOnes = 0
            iterationPlace = iterationPlace + 1
    return CountOfOnes


GetData = getData('14_steps.csv')
GetStartAndStop, standerDV = StartingandStopingPointFinder(GetData)
GetSlop = getSlop(gaussian_filter1d(GetStartAndStop, sigma = 4))
GetCount = CountTheOnes(GetSlop)
print(GetCount)


 
