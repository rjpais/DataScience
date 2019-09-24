# Making a scatter plot using pandas on large data datasets

%matplotlib inline
import numpy as np
import pandas as pd 

from matplotlib import pyplot as plot
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing data from csv into object
data = pd.read_csv("C:/Users...File.csv")
print (data.shape)    # prints data dimensions 
data.head()     # shows colunn names and first rows

# Fetching values of variables using pandas

F1 = data[ 'columNameX1'].values
F2 = data [ 'columNameX2'].values
X = np.array(list(zip(F1, F2) ))
plt.scatter(F1, F2, color = "blue", s = 7)
plt.show()   
