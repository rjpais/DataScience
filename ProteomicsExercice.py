# Import cvs data set
import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import sys

Tk().withdraw()
path = askdirectory(title ="Chose folder where the proteomics data set is located" )
DATAfile = open (path + "/proteins_time_course.csv", "r")   
Dataset = []
Features = []
k = 0
for line in DATAfile:
    data = line.split(",")
    if k == 0 :
        Features = data
    if k > 0:
        if [2][0] != "#": 
            Dataset.append(data)
    k = k + 1
DATAfile.close()


print("                 DATA SET SUMMARY                    ")
print("======================================================")
print( "total number of protein hits =   ", len(Dataset) )
print( "total number of colum features  =   ",  len(Features))

for i, col in enumerate(Features):
    print("col index ", i," name : ", col  ) 
print("======================================================")



# Computing the main relative changes in expression for each protein  
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 10)

#Cutoffs setting 
minCov = 15   #  minimum coverage threshold 
minSel = 20   # minimal % variation of expression for selectig proteins 


PVAR= []  # list with max relatve expression of protein
DREG = []  # Lis for dowregulations 
ProtGroups = []  
ProtFunc = []
COVERAGEData = []
countHighVar = 0
countHighCov = 0 
# parsing the data set and make calulation and removing low expression/bad ones 
for data in Dataset:
    ID = data[1]
    Group = data[0]
    Function = data[6]
    Descrip = data[8]
    Areas = [float(A) for A in data[9:20] ]
    Coverages = [float(C) for C in data[20: len(data)] ]
    for cov in Coverages:
        COVERAGEData.append(cov)
    TotalAreas = sum(Areas)
    if TotalAreas >0:
        maxVARp = (max(Areas) - min(Areas))/ sum(Areas) * 100
        Dowreg = (Areas[0] - min(Areas))/ sum(Areas) * 100
    if TotalAreas == 0:
        maxVARp = 0
        Dowreg = 0
    AvCoverage = sum(Coverages)/11
    if AvCoverage >= minCov:
        countHighCov = countHighCov + 1
    if maxVARp >= minSel:
        countHighVar = countHighVar +1
    if AvCoverage >= minCov and maxVARp >= minSel:
        PVAR.append([maxVARp, ID, Group, Descrip, Function, AvCoverage ])
        if Function not in ProtFunc:
            ProtFunc.append(Function)
        if Group not in ProtGroups:
            ProtGroups.append(Group) 
    if AvCoverage > minCov and Dowreg < 0:
        DREG.append([Dowreg, ID, Group, Descrip, Function, AvCoverage ])    


# Ploting the distribution of average coverage
density = stats.kde.gaussian_kde(COVERAGEData )
x = np.arange(min(COVERAGEData), max(COVERAGEData), 1)
plt.plot(x, density(x), label = "proteomic data",linewidth = 3 )
Y= [k/1000 for k in range (0,1000) ]
plt.plot([minCov for x in Y],Y ,"k--" , linewidth = 3, label = "cut-off" )
plt.xlabel('Mean coverage' , size = 20)
plt.title("Distribution of mean coverages on proteomics  ", size =24)
plt.ylabel('frequency' , size = 20)
plt.tick_params(axis='both', labelsize = 20) # set the font of axis values
plt.legend( fontsize = 20)
plt.axis([min(COVERAGEData), max(COVERAGEData), 0, 0.14]  )
plt.show()
    
#=========================================================================================================
#=========================================================================================================



# Computing Venn diagram with selected data hits
 
from matplotlib_venn import venn2
A = countHighVar - len(PVAR)
B = countHighCov - len(PVAR)
L1 = "> " +str(minSel) + "% relative expression variation "
L2 = "> " +str(minCov) + "% average coverage"
C = len(PVAR)
venn2(subsets = (A, B , C), set_labels = (L1, L2))
plt.show()
print ("\n=====================================================================" )
print("% proteome with resonable coverage                    ",
      int( countHighCov/len(Dataset)*100), " %" ) 
print("% proteome with high expression                       ", 
      int(countHighVar/len(Dataset)*100), " %" ) 
print("% proteome with expression reduction  =               ", 
      int(len(DREG)/len(Dataset)*100), " %  " )
print("% proteome with high expression + resonable coverage  ", 
      int(len(PVAR)/len(Dataset)*100), " % " )

print ("=====================================================================" )



#Ordering lists for best candidates
PVAR = sorted(PVAR, reverse=True )
DREG = sorted(DREG, reverse=False )

# computed percentils Expression increase 
P99 =  np.percentile(np.array([x[0] for x in PVAR ]), 99)
P95 =  np.percentile(np.array([x[0] for x in PVAR ]), 95)
P90 =  np.percentile(np.array([x[0] for x in PVAR ]), 90)
P75 =  np.percentile(np.array([x[0] for x in PVAR ]), 75)
P50 =  np.percentile(np.array([x[0] for x in PVAR ]), 50)
P25 =  np.percentile(np.array([x[0] for x in PVAR ]), 25)

""" 
P99d =  np.percentile(np.array([x[0] for x in DREG ]), 99)
P95d =  np.percentile(np.array([x[0] for x in DREG ]), 95)
P90d =  np.percentile(np.array([x[0] for x in DREG ]), 90)
P75d =  np.percentile(np.array([x[0] for x in DREG ]), 75)
P50d =  np.percentile(np.array([x[0] for x in DREG ]), 50)
P25d =  np.percentile(np.array([x[0] for x in DREG ]), 25)
"""
print("\n\nPercentils for selecting the threshold of highly response proteins: ")
print("\t99 percentil = ", int(P99), "%")
print("\t95 percentil = ", int(P95), "%")
print("\t90 percentil = ", int(P90), "%")
print("\t75 percentil = ", int(P75), "%")
print("\t50 percentil = ", int(P50), "%")
print("\t25 percentil = ", int(P25), "%")
#print("\t99 percentil = ", int(P99d), "%")
#print("\t95 percentil = ", int(P95d), "%")
#print("\t90 percentil = ", int(P90d), "%")
#print("\t75 percentil = ", int(P75d), "%")
#print("\t50 percentil = ", int(P50d), "%")
#print("\t25 percentil = ", int(P25d), "%")

print("\n        TOP Protein > 55% variation   (percentil 95%)                 ")
print ("% VAR   Prot ID       GroupID           Desription     ")

PS_IDS = []
for P in PVAR:
    if P[0] > 55:
        PS_IDS.append(P[1])
        print (int(P[0]),"    \t" , P[1],"   \t" ,  P[2], "   " , P[3][0:70] )   
print ("======================================================================" )
print ("Total proteins selected = ", len(PS_IDS)) 




  
#=========================================================================================================
#=========================================================================================================



# MAKING A PLOT with main proteins  THAT COMPOSE CANCER DIAGNOSTIC MODELS with tags   



# get time times series of selected proteins
Time = [0, 0.5, 1, 2, 3, 4, 5, 6, 9, 12, 24]
for data in Dataset:
    ID = data[1]
    if ID in PS_IDS:
        Areas = [float(A) for A in data[9:20] ]
        TotalAreas = sum(Areas)
        RelativeAreas =  [A/TotalAreas*100 for A in Areas ]
        plt.plot(Time, RelativeAreas, linewidth = 3, label = "protein ID " + ID  )
plt.xlabel('Time (hours)' , size = 20)
plt.title("Time-course main proteins expression response to therapy ", size =24)
plt.ylabel('Relative protein Expresion (%)' , size = 20)
plt.tick_params(axis='both', labelsize = 20) # set the font of axis values
plt.legend( fontsize = 10)
plt.axis([0, 24, 0, 100,]  )
plt.show()



  
#=========================================================================================================
#=========================================================================================================


# Analyzing groups and functions frequencies in changed expression proteins

print ("PROTEIN GROUPS DETECTED WITH COUNTS > 1")
print("=================================================")
GrupCounts = []
GroupFreq = [ F[2] for F in PVAR] 
for G in  ProtGroups:
    c = GroupFreq.count(G)
    GrupCounts.append(c)
    if c > 1:
        print ("protein group ", G, " Count  = ", c )
print("=================================================")



FunctCounts = []
FunctFreq = [ F[4] for F in PVAR]   
for F in  ProtFunc:
    c = FunctFreq.count(F)
    FunctCounts.append(c)
PlotNames = []    
for name in ProtFunc:
    if name == "":
        name = "Unknown"
    PlotNames.append(name)
    
plt.bar( np.arange(len(ProtFunc)), FunctCounts , color = "orange")
plt.xlabel('PTM' , size = 20)
plt.title("PTM associated with high expression response  ", size =24)
plt.ylabel('Counts ' , size = 20)
plt.tick_params(axis='both', labelsize = 20) # set the font of axis values
plt.xticks(np.arange(len(ProtFunc)), PlotNames , fontsize=16, rotation = 90)

plt.show()

    








