#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value of the day:'))
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    test_dict={}
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if row_date<start_date:
            continue
        if row_date>=start_date:
            if row_date not in test_dict:
                test_dict[row_date]=[row[0]+' '+row[1]]
            else:
                dict_name=test_dict.get(row_date)
                dict_name.append(row[0]+' '+row[1])
                test_dict[row_date]=dict_name

    return test_dict

def list_newer(start_date):
        #print(start_date)
    name_dict=get_same_or_newer(start_date)
 #   print(name_dict)
    for i in sorted(name_dict.keys()):
         print("Started on {}: {}".format(i.strftime("%b %d, %Y"), name_dict[i]))

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()

    
