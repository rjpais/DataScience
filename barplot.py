# a simple  barplot 
import matplotlib.pyplot as plt
    
# use a predifined style of plots ( this case ggplots from R)
plt.style.use('ggplot')


Players = [ "Ricardo", "Mike", "Tiago", "Pedro", "Mauro", "Vasco" ] # variable x
Golos = [ 1,  4,  5,  2 , 6, 3 ]      # variable y  


# title of plot
plt.title("Goals of VOLTAR N players in last game")

# axis lables 
plt.xlabel("Players")
plt.ylabel("Goals")

# plot and show data
plt.bar(Players, Golos, color = "orange")
plt.show()  

