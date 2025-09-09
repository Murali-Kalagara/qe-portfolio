import os
import csv

file_path = file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day 5', 'write_numbers.csv'))
with open(file_path,'w') as file:
    input = [1,2,3,4,5,6,7,8,9]
    conv_input = ','.join(str(num) for num in input)
    file.write(conv_input)