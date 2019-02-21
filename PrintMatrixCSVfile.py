"""
Script that demonstrates how to generate and print a matrix to csv file in python 2.7 Version
"""
A = range(1,3000,2) # set as the number of rows
B = range(1,200,1) # set as the rows of colums

# Generation of a matrix of data in a list that relates variables A and B by Y = 2*A + B
DATA = []
for i in A:        #  i is each rows
    Ci = []
    for j in B:    # j is each column
        y= 2*i + j
        Ci.append(y)
    DATA.append(Ci)


# function to write each row of csv
def csv_row(col1, colvalues):
	# makes a row for csv files taken with a row name in 1 column and values (col1) of a list in the folowing columns (colvalues)
	sample_row= ""
	for value in colvalues:
		sample_row = sample_row + str(value) + ","
	row = str(col1) + "," + sample_row[0:-1] +  "\n"
	return row


# for writing a single matrix of data in a csv file and close it
outfile = open("matrixData.csv", "w")
header = csv_row("dataij",B)
outfile.write(header)
for i, coli in enumerate(A):
    rowi = csv_row(coli, DATA[i])
        Outfilei.write(rowi)
Outfilei.close()
