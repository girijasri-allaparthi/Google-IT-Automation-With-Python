#!/usr/bin/env python3
import sys
import csv
from pathlib import Path

def error_handling_func(name):
    try:
        filepath=Path.cwd()/Path('OneDrive//Desktop//emailexcel.csv')
        with open(filepath) as file:
                  file_data=csv.DictReader(file)
                  for data in file_data:
                            #assert type(name[1])==str, 'Please enter the valid name format'
                            if type(name[1])!=str:
                                raise ValueError("please enter the valid name format")
                            if data['Full Name']==sys.argv[1]+' '+sys.argv[2]:

                                return data.get('Email Address')
    except FileNotFoundError:
        print("please check the file path you provided")
    except IndexError:
        print("please enter First name and last name")

error_handling_func(name)
