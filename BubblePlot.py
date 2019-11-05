# HOW TO MAKE of a bubble plot using a scatter plot
# save figures and redimention axis plots 

import matplotlib.pyplot as plt
    
# use a predifined style of plots ( this case ggplots from R)
plt.style.use('ggplot')


A = [ 1 ,  2,  3, 4, 5 , 6,   7,    8,     9,  10]         # variable x
L  =[ 43 ,  30,  50, 40, 50 , 35,   70,    50,     30, 20]  # variable y
I = [30, 2000, 30,  3000, 6666 , 333,3333,33, 344, 400]   # size of the bubble 


# title of plot
plt.title(" a bubble plot example", fontsize = 16)

# axis lables 
plt.xlabel("x-axis", fontsize = 14)
plt.ylabel("y-axis", fontsize = 14)


# Reedimention font of axis and values
plt.xlim((0, 11))   # set the x limits to bottom, top
plt.ylim(0, 80)     # set the y limits to bottom, top
plt.tick_params(axis='both', labelsize=14) # set the font of axis values

plt.scatter(A, L, marker = "." ,  s = I, color = "#621054" ) # note size of  will be equal to a list of weights
plt.savefig("figure1.png", dpi = 900)
