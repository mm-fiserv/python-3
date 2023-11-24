from ValidationException import ValidationException

import csv

def ex1():
    try:
        validate_file('python-3-main/files/input.txt')
    except ValidationException as ve:
        print("Error: Invalid entry")

def validate_file(file_name):
    line_count=0
    with open(file_name) as csv_file:
        validate = csv.reader(csv_file, delimiter=',')
        for row in validate:
            if line_count==0:
                line_count+=1
            else:
                if (row[0].isnumeric() and row[1].strip().isnumeric()):
                    print("is int")
                else:
                    print("not int")

ex1()