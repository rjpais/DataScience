# plot of curves using python with ggplots style 

import matplotlib.pyplot as plt

# use a predifined style of plots ( this case ggplots from R)
plt.style.use('ggplot')

# lists of values of variables 
X = [ xi for xi in range(0, 100) ] # independent variable x 
Y = [ float (200*xi^2) / ( xi  + 20)  for xi in X ] # Hyperbolic function (dependent variable)
K  = [ 100  for xi in X ]      # constant function  (dependent variable)
Z = [ 3*xi + 3  for xi in X ]  # linear function  (dependent variable)

# a way of intercepting functions 
I = [xi for i, xi in enumerate(X) if round(Y[i], 0) == round(Z[i], 0) ] # get the maching values of Y and Z functions   
print ("intercept Y with Z : x  = ", max(I) )


# title of plot
plt.title("intercept of functions")

# axis lables 
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# plot and show data
plt.plot(X, Z, color = "red", label = "linear", linestyle = "--" )
plt.plot(X, Y, color = "blue", label = "hyperbolic")
plt.plot(X, K, "k--", label = "constant", linestyle = ":")
plt.scatter(X, Y, color = "black", marker = ".", s = 20 )
plt.legend()
plt.show()  
