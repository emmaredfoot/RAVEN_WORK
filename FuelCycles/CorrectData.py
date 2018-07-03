# First Read in the data
# Then take the second column and multiply it by .056
import csv
import os
import string

def writeFile(filename, outfile):
    dataset = csv.reader(open(filename))
    with open(outfile, 'w') as subfile:
    # Rewrite the first column in the eia data so that it gives the year, the month and day, and the times
        subfile.writelines('Time,Demand'+os.linesep)
        for row in dataset:
            demand = row[6]
            NukeDemand=float(demand.strip(''))*.056
            print(NukeDemand)
            subfile.writelines('{0},{1}'.format(row[1], str(NukeDemand)+os.linesep))




Spring = writeFile('Spring-2017.csv','spring/SpringDemand.csv')
Summer = writeFile('Summer-2017.csv','summer/SummerDemand.csv')
Fall =  writeFile('Fall-2017.csv','fall/FallDemand.csv')
Winter = writeFile('Winter-2017.csv','winter/WinterDemand.csv')
