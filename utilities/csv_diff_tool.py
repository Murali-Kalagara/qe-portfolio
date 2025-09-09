import os
import csv
file_path_a = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sample_csvs', 'File_A.csv'))
file_path_b = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sample_csvs', 'File_B.csv'))
customer_id_a = set()
customer_id_b = set()

#Finding the missing keys in File A and File B
with open(file_path_a,'r') as file_a:
    reader_a = csv.DictReader(file_a)
    for row in reader_a:
        customer_id_a.add(row['Customer Id'])

with open(file_path_b,'r') as file_b:
    reader_b = csv.DictReader(file_b)
    for row in reader_b:
        customer_id_b.add(row['Customer Id'])

missing_customer_id_file_a = customer_id_b - customer_id_a
missing_customer_id_file_b = customer_id_a - customer_id_b

print(missing_customer_id_file_a)
print(missing_customer_id_file_b)

#Function to build dictionary from csv



def build_dict(file_path):
    result_dict = {}
    with open(file_path,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer_id = row['Customer Id']
            row_data = dict(row)
            del row_data['Customer Id']
            result_dict[customer_id] = row_data
    return result_dict

dict_a = build_dict(file_path_a)
dict_b = build_dict(file_path_b)

print("Dict A:", dict_a)
print("Dict B:", dict_b)