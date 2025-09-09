import os
import csv
from datetime import datetime

file_path =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day 5', 'write_numbers.csv'))
with open(file_path,'a') as file:
    file.write("\n Test with current time" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))