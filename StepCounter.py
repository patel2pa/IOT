
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
from scipy import signal
import statistics 

data = pd.read_csv('14_steps.csv')
 
x = []
 
for d in range(len(data['x'])):
    #print(data['x'][d])
    mag = (data['x'][d])**2 + (data['y'][d])**2 + (data['z'][d])**2
    x.append(math.sqrt(mag))
 
 
 
ysmoothed = gaussian_filter1d(x, sigma = 4)


def StartingandStopingPointFinder(SmoothedArray):
    
    slopChanges = []
    count = 0
    while count < len(SmoothedArray):
        
        slopChanges.append(statistics.stdev(SmoothedArray[count:count+5]))
        count = count + 5

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
            
        if NonZeros[0]>20:
            starting = NonZeros[1]
            startingPointFound = True
            
        if startingPointFound == True and zeros[0] > 3:
            ending = zeros[1]
            endingPointFound = True
            
        if endingPointFound == True:
            break
            
    print(NonZeros)
    print(zeros)
    print(slopChanges)
    print(starting)
    print(ending)
    return SmoothedArray[starting*5:ending*5]
    
        
            
    
  
plt.plot(gaussian_filter1d(x, sigma = 4))  
b = StartandStopValues(x)
plt.plot(gaussian_filter1d(b, sigma = 4))
        
            
plt.show()
