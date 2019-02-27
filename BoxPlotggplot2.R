
library(ggplot2)

#import data (data frame) from a csv file 
data <-  read.csv (file.choose())

# Generate a simple boxplot of variable 2 (y)  mapped with variable 1 (x) using ggplot2.
BP <- ggplot(data, aes(x=as.factor(variableName1), y=variableName2)) +    
  geom_boxplot(fill="yellow", alpha=0.2) + 
  xlab("name of variable 1")

# Showing the Box plot with the data overlaping
BP + geom_jitter(shape=16, position=position_jitter(0.2), color = "darkblue")

