# Table of Contents
1. [Approach](README.md#Approach)
2. [Dependencies](README.md#Dependencies)
3. [Run Instructions](README.md#Run-Instructions)


#  Approach

There are mainly xxx parts for the approach here:
* Step1: read in each line of information from log.csv file, and the inactivity_period info from inactivity_period.txt file. Then store the log information in a list called 'data'
* Step2: scan through each element in data list, create a dictionary using IP address as the key, the rest of the information as its values. There are 2 scenarios for information with new IP address and information with existing IP address.
*  Step3: A list called new_list is created using the processed key-value pair in dictionary. The calculation of time difference(delta) between current time to the time the IP first access the website is performed for each element in new_list.
* Step4: using delta, 2 new lists(res_list1, res_list2) are created to stored records whose latest activity has passed the inactivity_period and within inactivity_period. Then res_list1 is sored by delta descending, and res_list2 is sorted by first access time and then last access time.
* Step5: result list combines information from res_list1 and res_list2, and then print out to sessionization.txt file in output folder.

# Dependencies

As the program is written in python3, below modules and libraries are used:

Modules:
* os
* csv
* operator
* datetime

# Run Instructions

Simply go to folder /edgar-analytics-master, then run ./run.sh


For further questions,  please email me at `qiandongmin@gmail.com`.
