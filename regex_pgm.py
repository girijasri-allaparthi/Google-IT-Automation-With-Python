#!/usr/bin/env python3

import os
import re
import csv

#### This program reads the logfile######
#### Using regular expressions it collects the Error messages####
#### Writes the Error messages and number of occurances into CSV file####
def check_errors(filename):
   # with open('/home/student-04-b2bdd7022a3c/file','r') as file:
    with open(filename,'r') as file:
        data=[]
        for line in file.readlines():
            pattern=r'(ERROR )([\w+\s\']+)'
            try:
                result=re.search(pattern,line)
                data.append(result[2])
            except TypeError:
                continue

    data1={}
    for i in data:
        data1[i]=data1.get(i,0)+1
    error={}
    for i in sorted(data1,key=data1.get,reverse=True):
        error[i]=data1.get(i)
    mylist=[]
    for i in error.keys():
        mylist.append({'Error':i,'Count':error.get(i)})
 #   with open('/home/student-04-b2bdd7022a3c/error_message.csv','w+',newline='')as file:
    with open(os.getcwd()+'\\OneDrive\\Desktop\\error_message.csv','w+',newline='')as file:    
        fieldnames=["Error","Count"]
        writer=csv.DictWriter(file,fieldnames)
        writer.writeheader()
        writer.writerows(mylist)
