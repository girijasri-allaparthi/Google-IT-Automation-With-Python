#!/usr/bin/env python3

######This program is used to upload the image to the website with provided URL##########
import os
import requests
listimages_jpeg=os.listdir('/home/student-04-1c6cbe55ad0c/supplier-data/images')
url="http://34.16.184.23/upload"
def image_upload(listimages_jpeg):
        for i in listimages_jpeg:
                if '.jpeg' in i:
                        with open(os.path.join('/home/student-04-1c6cbe55ad0c/supplier-data/images',i),encoding='utf-8', errors='ignore') as opened:
                                r=requests.post(url,files={'file':opened})
                                print(r.ok)
                                print(r.status_code)
image_upload(listimages_jpeg)
