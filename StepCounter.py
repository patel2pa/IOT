
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
from scipy import signal
data = pd.read_csv('14_steps.csv')
 
x = []
 
for d in range(len(data['x'])):
    #print(data['x'][d])
    mag = (data['x'][d])**2 + (data['y'][d])**2 + (data['z'][d])**2
    x.append(math.sqrt(mag))
 
 
 
ysmoothed = gaussian_filter1d(x, sigma = 4)
plt.plot(ysmoothed)



def SlotAnalysis(SmoothedArray):
    
    slopChanges = []
    for num in SmoothedArray:
        
        
    print(SmoothedArray)

    
#StartCounting(yysmoothed)   


newArray = []
        
#for num in range(len(yysmoothed)):
    
        
plt.show()


'''
 
test = []
for z in range(len(yysmoothed)):
    if z == 0:
        continue
    else:
        test.append((yysmoothed[z]-yysmoothed[z-1])/1)
 
plt.plot(test)
plt.show()
'''
 
'''
from __future__ import division
  
import numpy as np
  
fL = 0.1  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
fH = 0.4  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
b = 0.08  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
N = int(np.ceil((4 / b)))
if not N % 2: N += 1  # Make sure that N is odd.
n = np.arange(N)
  
# Compute a low-pass filter with cutoff frequency fL.
hlpf = np.sinc(2 * fL * (n - (N - 1) / 2))
hlpf *= np.blackman(N)
hlpf /= np.sum(hlpf)
  
# Compute a high-pass filter with cutoff frequency fH.
hhpf = np.sinc(2 * fH * (n - (N - 1) / 2))
hhpf *= np.blackman(N)
hhpf /= np.sum(hhpf)
hhpf = -hhpf
hhpf[(N - 1) // 2] += 1
  
# Add both filters.
h = hlpf + hhpf
'''
 
'''
import scipy
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
def butter_bandpass(lowcut, highcut, fs, order=5, label=None):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = signal.butter(order, [low, high], btype='band', output='sos')
    w, h = signal.sosfreqz(sos,worN=20000)
    plt.semilogx((fs * 0.5 / np.pi) * w, abs(h), label=label)
    return sos
 
center_freqs = np.array([0.5* 2 ** (n * 1 / 3.) for n in range(0, 29)])
center_freqs.sort()
lower_freqs = 2. ** (-1 / 6.) * center_freqs
for lf in lower_freqs:
    butter_bandpass(lf, lf*2**(1/3.), fs=1000, order=5)
 
plt.show()
'''
