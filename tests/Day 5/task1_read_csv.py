import os
import csv
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day 5', 'employees.csv'))

with open(file_path,'r') as file:
   reader = file.read()
   print(reader)
"""final_file = csv.reader(file)
    next(final_file)
    for row in final_file:
        print(row)"""


# if we dont need the output to be printed in list and wants in original format

    
"""with open(file_path,'r') as file:
    final_file = csv.reader(file)
    next(file)
    for row in file:
        print(row.strip())"""
