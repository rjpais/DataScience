"""
Function to estimate the probability of a given  outcome given specific tresholds
and assuming a normal distribution
Example of the probabilities of a genetic blood abnormality
"""
import numpy as np
import scipy
from scipy.stats import norm


#--------------------------------------------------------------------
# Function for estimating the probability of an outcome
# based on the gausian deviation from the maximum probability on the density function
#--------------------------------------------------------------------
def Prob_Outcome(xi, Xm, std, L, type):
    # xi variable to estimate the probability
    # Xm -> expected value (average of normal/ reference value) colums names,
    # std -> the stander deviation for normality
    # L ->  left/ right/ both tails choice (takes values -1, 1, 0 respectively)
    # type of test far (1) or close to expected (0) from expected value
    if xi != "na":
        Pref = scipy.stats.norm(Xm, std).pdf(Xm)
        if L == 1:
            if xi >= Xm and xi <= (Xm + 4*std):
                Px = float(scipy.stats.norm(Xm, std).pdf(xi)) / Pref
            elif xi < Xm:
                Px = 0
            else:
                Px = 1
        if L == -1:
            if xi <= Xm and xi >= (Xm - 4*std) :
                Px = float(scipy.stats.norm(Xm, std).pdf(xi)) / Pref
            elif xi > Xm :
                Px = 1
            elif xi < (Xm - 4*std) :
                Px = 0
        if L == 0:
            if xi > (Xm - 4*std) and xi < (Xm + 4*std):
                Px = float(scipy.stats.norm(Xm, std).pdf(xi)) / Pref
            else:
                Px = 0
    else:
        Px = 0.5
    return abs(type - Px)
#--------------------------------------------------------------------


#--------------------------------------------------------------------


# Probability estimation of a abormality

print "Example 1: probability of being normal, considering both tails :"
samples = [369.1, 370.2, 366.2, 377.5, 345.9, 367.8, 600, 310]
for x in samples:
    Px = Prob_Outcome(x, 368 , 6 , 0, 0 )
    print "p (" , x , ") = ", Px

print "\nExample 2: probability of having a specific type of blood disorder, considering left tail"
for x in samples:
    Px = Prob_Outcome(x, 368 , 6 , -1, 0 )
    print "p (" , x , ") = ", Px

print "\n Example 3: probability of having a specific type of blood disorder, considering right tail"
for x in samples:
    Px = Prob_Outcome(x, 368 , 6 , 1, 1 )
    print "p (" , x , ") = ", Px
