# Example of box plots similar than ggplots in R using python 
# also make a random generation of a dummy data set 

import matplotlib
import matplotlib.pyplot as plt
import random 

    
# use a predifined style of plots ( this case ggplots from R)
plt.style.use('ggplot')


Data = []   
VARIAV = []

# generate dummy data sets for box plots with a given variability
for i in range(5):  # number of total data sets
    DataSet = []
    VARIAV.append("SET- "+ str(i+1))
    for j in range(10): # number of total samples in each data set
        DataSet.append(random.random() * float(i+2)/4 + 10)
    Data.append(DataSet)

# title of plot
plt.title("comparison of 2 sets")

# axis lables 
plt.xlabel("sets")
plt.ylabel("values")

# plot and show data
box1 = plt.boxplot(Data,
           notch=True,  # notch shape
            vert=True,  # vertical box alignment
            patch_artist=True,  # fill with color
            labels=VARIAV,
           flierprops = dict(markerfacecolor='k', marker='.')  # make full colored customized outliers
                    )

for patch in box1['boxes']:
    patch.set_facecolor('yellow')
plt.show()


box2 = plt.boxplot(Data,
           notch=False,  # notch shape
            vert=False,  # vertical box alignment
            patch_artist=True,  # fill with color
            labels=VARIAV,
           flierprops = dict(markerfacecolor='k', marker='.')  # make full colored customized outliers
           )

# fill with different colors
colors = ['pink', 'lightblue', 'lightgreen', 'yellow', 'red']
for patch, color in zip(box2['boxes'], colors):
    patch.set_facecolor(color)
    
plt.show()
