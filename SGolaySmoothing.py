
#--------------------------------------------------------------------
# function for Smoothing with Savistky Golay filter
#--------------------------------------------------------------------
import scipy
from scipy import signal
def smoothing_data(mzwin, p10, ncycles, Intensities):
    # sooths the data using savinsky gollay filter given a mz size window and number of cycles
    # p10 is the number of points in the range of 10 units in the x-axis  
    nw = int(mzwin * p10 / 10)   # Calculate the wiwndow size in number of points
    Smoothed = Intensities
    if nw % 2 == 0:             # keeps the window always an odd number not to crash algorithm
        nw = nw + 1
    Smoothed = scipy.signal.savgol_filter(Smoothed, nw, ncycles)  # performs the Savitsky Golay filter
    return Smoothed
#--------------------------------------------------------------------


# EXAMPLE with dummy data with random noise addition to a function

import numpy as np
noise = np.random.normal(0,1,10000)

X = range(0,10000,1)  
DATA = [] 
for i, x in enumerate(X):
  y = 0.001*x**3 + noise[i]   

Sdata = smoothing_data(2, 2 , 5, DATA)

