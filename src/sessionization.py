## Sessionization.py for Edgar-Analytics-Master challenge
import os
import csv
from datetime import datetime, timedelta
datetime_format = "%Y-%m-%d %H:%M:%S"

## data formate initialization
data =[] #a list to store info from each row in log.csv file
dict = {} #dicionary to use IP as key, and other info as its values.
result = [] #list to store final results
new_list = [] #list to store the processed log record.


## path setting for data reading and result output
cur_path = os.getcwd() #get current working directionary path
file_path1 = os.path.join(cur_path, "input", "inactivity_period.txt")
file_path2 = os.path.join(cur_path, "input", "log.csv")
file_path3 = os.path.join(cur_path, "output", "sessionization.txt")

## read in inactive period value from inactivity_period.txt file
f1 = open(file_path1,'r')
inactivity_period = int(f1.readline())

## read in raw data from log.csv file
f2 = open(file_path2,'r')
rawdata = csv.reader(f2)

## Remove the empty line in log.csv
for row in rawdata:
    if row != []:
        data.append(row) #data is a list data structure

## read log entry from line2 (index 1), and scan through each line of log
for i in range(1,len(data)):
    row = data[i]
    key = row[0] #key = IP address
    timestamp = datetime.strptime(row[1] + ' ' + row[2], datetime_format)

    ## check if the IP is a new record or has already exit in dict key
    if key not in dict.keys():
        ## key values in order: 0:st-time,1:ed-time, 2:filename, 3:file type, 4:access time,
        ## 5:number of file accessed, 6:time diff= save as zero for now
        dict[key] = [timestamp,timestamp,row[5],row[6],1,1,0]

    else:
        ## if the IP already exists in curr_dict key
        ## chech if it passes the inactivity_period since last visit
        diff = timestamp - dict[key][1] #### diff = current timestamp - last time visited
        access_time = diff.seconds

        ## if this acess is within the inactivity_period, then update the existing record in dict
        if access_time <= inactivity_period:
            dict[key][0] = dict[key][0] #first request time #####
            dict[key][1] = timestamp #last request time

            # update time elapsed : diff = last request time - first request time
            dict[key][4] += access_time

            # Update the file accessed and the number of file accessed
            dict[key][2] = row[5]
            dict[key][3] = row[6]
            # update the number of file accessed
            dict[key][5] += 1
            # time diff, save as zero for now
            dict[key][6] = 0

        ## if this visit has pasted the inactivity peropd, then append the exisiting record to new_list,
        ## then create a new IP entry in dict
        else:
            new_list.append([key,dict[key]])
            dict[key] = [timestamp,timestamp,row[5],row[6],1,1,0]

# scan thru all key-value pair from dict to new_list
for key in dict.keys():
      new_list.append([key,dict[key]])

## create two list to store records passed inactivity_period
## and record have not passed the inactivity_period.
res_list1 = [] # for records passed inactivity_period
res_list2 = [] # for records have not passed inactivity_period

## scan thru the new_list, to calculate the delta time = current_timestamp - first access time
## then ass this delta to the end of new_list
for item in new_list:
    delta = (timestamp-item[1][1]).seconds
    item[1][6] = delta

    ## determine if the record passed the inactivity_period or not
    ## if passed, store in res_list1, if not passed, store in res_list2
    if delta > inactivity_period:
        res_list1.append([item[0],item[1][0],item[1][1],item[1][4],item[1][5],item[1][6]])
    else: #delta <= inactivity_period
        res_list2.append([item[0],item[1][0],item[1][1],item[1][4],item[1][5],item[1][6]])

from operator import itemgetter
## order res_list1 by descending of delta time
res_list1 = sorted(res_list1,key=itemgetter(5),reverse=True)
## order res_list2 by st_time and ed_time
res_list2 = sorted(res_list2,key=itemgetter(1,2))

## combine the two soreted list as final result list
for item in (res_list1 + res_list2):
    result.append(item[:5])

## write result to sessionization.txt
import datetime
format11 = '%Y-%m-%d %H:%M:%S'

f3 = open(file_path3,'w')
with f3 as f:
    for item in result:
        item[1] = item[1].strftime(format11)
        item[2] = item[2].strftime(format11)
    wr = csv.writer(f,lineterminator='\n')
    wr.writerows(result)
f3.close()
