# a  barplot with classes 

import matplotlib.pyplot as plt
    
# use a predifined style of plots ( this case ggplots from R)
plt.style.use('ggplot')


Pontas = [ "Ricardo", "Tiago" ] # variable x
MeiaDist = [ "Pedro", "Mauro", "Vasco" ] # variable x
Pivot = [ "Mike" ] # variable x
GolosPont = [ 1,  4 ]      # variable y  
GolosMeia = [ 2 , 6, 3 ]      # variable y  
GolosPiv = [ 5 ]      # variable y  


# title of plot
plt.title("Goals of VOLTAR N players in last match")

# axis lables 
plt.xlabel("Players")
plt.ylabel("Goals")

# plot and show data
plt.bar(Pontas, GolosPont, color = "cyan", label = "Wing")
plt.bar(MeiaDist, GolosMeia, color = "blue", label =  "Back" )
plt.bar(Pivot, GolosPiv, color = "green", label =  "Line") 
plt.legend()
plt.show()  
