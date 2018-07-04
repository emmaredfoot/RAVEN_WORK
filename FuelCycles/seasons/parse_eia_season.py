
import datetime as dt
import time as tmod
import numpy as np
import os
import string

def readData(Dataset):
    print 'reading',Dataset,'...'
    #Dictionary to store results with keys time and demand
    data = {'time':[], 'demand':[]}
    #flag for when we start reading data
    start=False
    #keep file open to read from
    with open(Dataset, 'r') as infile:
        #loop over lines in filename
        #enumerate counts the number of lines, saves the counter to l
        #Saves the content of the line to value
        for counter,value in enumerate(infile):
            # if line is empyt, skip it
            if value.strip() == '':
                continue
            # if we're not started but we find the start, read in headers and trigger a start
            if not start and value.split(',')[0]=='Dates':
                headers = list(h.strip() for h in value.split(','))
                print 'headers: ', headers
                start = True
                firstTime = None
                continue
            # get the time, demand
            value = value.split(',')
            HE,PGE = list(float(counter) for counter in  value[0:2:1])
            time=int(HE)
            ##get demand
            data['time'].append(time)
            data['demand'].append(PGE)

        return data

def fixData(times, demand, interval, start, end):
    #print 'demand: ', demand
    newdemand = {}
    newtimes = {}
    #fix each year/period individually
    for year in alltimes.keys():
        print 'Fixing up', year, '...'
        low = 0.0
        high = low + interval
        ydemand = np.array(demand[year])
        ytimes = np.array(times[year])
        newdemand[year] = []
        newtimes[year] = []
        # loop through year and collapse interval
        counter = 0

        while high <= end:
            counter = counter+1
            newtimes[year].append(low)
            condition = (low<=ytimes*3600)*(ytimes<high)
            newdemand[year].append(np.average(np.extract(condition, ydemand)))
            #print 'extract', np.extract(condition, ydemand)
            #print 'check: ', newdemand[year]
            low = high
            high += interval

        return newdemand, newtimes

def writeData(times, demand, outname):
    print "Writing",outname,'...'
    with open(outname, 'w') as outfile:
        #write main file
        outfile.writelines('period,scaling,filename'+os.linesep)
        for k,key in enumerate(alldemand.keys()):
            subfilename='summer-out.csv'.format(outname[:-4],str(k+1))
            outfile.writelines('Time, Scaling, Demand'.format(key, 1, subfilename)+os.linesep)
            with open(subfilename,'w') as subfile:
                subfile.writelines('Time,Demand'+os.linesep)
                for i in range(len(times[key])):
                    #print "demand[key]: ", demand
                    subfile.writelines('{0},{1}'.format(times[key][i], demand[key][i])+os.linesep)



if __name__=='__main__':
    datasets = ['Summer-1003.csv']

#Create a dictionary called alldemand. Dictionaries are indexed by keys
alldemand = {}
alltimes = {}
for d in datasets:
    new = readData(d)
    #print "new: ", new
    alldemand[d.split('.')[0].split('-')[1]] = new['demand']
    #print 'alldemand: ', alldemand
    alltimes[d.split('.')[0].split('-')[1]] = new['time']

start = 0.0 # start time after data is converted
end = 5940000 # end time after data is converted
interval = 3600 # collapsing interval
alldemand, alltimes =  fixData(alltimes, alldemand, interval, start, end)
writeData(alltimes, alldemand, 'raw_data.csv')
