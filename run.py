#!/usr/bin/env python3

#######This program updates the image descriptions to the website############
import os
import requests
import json
url="http://34.16.184.23/fruits"
listtextfiles=os.listdir('/home/student-04-1c6cbe55ad0c/supplier-data/descriptions')
pdfdata=[]
def upload_descriptions(listtextfiles):
######This function reads the file contetnts and changes into a dictionary and uploads the######
######contents to the website#####
        for file in listtextfiles:
#                print(file)
                with open(os.path.join('/home/student-04-1c6cbe55ad0c/supplier-data/descriptions',file)) as f:
                        fread=f.readlines()
                        webdict={}
                        pdfdata1=[]
                        for i in fread:
 #                               print(i)
                                if fread.index(i)==0:
                                        webdict['name']=i.strip()
                                        pdfdata1.append('name'+':'+i.strip())
                                elif fread.index(i)==1:
                                        webdict['weight']=int(i.split()[0])
                                        pdfdata1.append('weight'+':'+i.strip())
                                else:
                                    if fread.index(i)==2:
                                        webdict['description']=i.strip()
                                    else:
                                        webdict['description']=webdict.get('description')+i.strip()
#                                print(file[:-4])
                        webdict['image_name']=file[:-4]+'.jpeg'
#                        print(webdict)

                pdfdata.append(pdfdata1)
                p=json.dumps(webdict)
                response=requests.post(url,data=p)
                print(response.ok)
                print(response.status_code)
                print(p)
                print(pdfdata)
upload_descriptions(listtextfiles)

