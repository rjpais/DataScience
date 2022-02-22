
# Perform U-test on a data set and get the pvalues



# open the data from csv files 
# select the csv files with data  
# needs to add correct data column intervals for positive and negative groups   

DATAin <-  read.csv (file.choose())

Positive <- as.data.frame(DATAin[2:54, 1:ncol(DATAin)-1])
negative <- as.data.frame(DATAin[55:ncol(DATAin), 1: ncol(DATAin)-1])
S = ncol(DATAin)-1

NAMES <- c(seq(1,ncol(DATAin)-1, by = 1))


Feature <-c ("Y Lable to add")


#==================================================================================================================
# Extracting p-values of the two-sample Wilcoxon tests 'Mann-Whitney'.

# matrix for the p values 

pvalues <- matrix(nrow = 1, ncol = S)  # Defining a matrix to put the p-values of U test
rownames(pvalues) <- c("U p-value")
Rank_pvalues = t(pvalues)
colnames(pvalues) <- c(NAMES)

# Calculating p values for each BIN and store it in a vector

for(i in 1:S) {pvalues[ ,i]<-wilcox.test(Positive[,i], negative[,i], alternative = "two.sided", conf.level = 0.95  )$p.value 
} 



# Show the  p values  on console 

pvalues

