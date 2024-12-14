#JUST A TESTING SITE
"""
import csv

from dir_manage import *
from pathstring import path_string"""
from time import process_time
from tokenize import endpats

'''l = list(range(0, 100))
s = '{}/'
def path_string(nested_dirs_list):
    p_str = '{}/'
    nested_dirs_list.pop()
    while nested_dirs_list:
        p_str += '{}'
        nested_dirs_list.pop()
        if nested_dirs_list:
            p_str += "/"
    return p_str


print(path_string(l))'''
import os

'''from os import getcwd

""" 
s = r'o{}'
s+=r'9999'
print(s.format(3))

"""

import os
print(getcwd())

print(list(map(lambda x:x,range(9))))
#print(type(*([0]+[2,3])))
help(type)'''
'''
if 1:
    print('j')'''
'''def path_string(dirs):
    """
    Generates a nested path string from the number of directories.
    """
    return "/".join(["{}"] * dirs)
print(path_string(8))'''
'''
while False:
    os.makedirs(r'/home/sahil/j/a',exist_ok=True)

def nested_dirs_creator(*dir_names):
    """
    :param dir_names: Variable length argument containing nested directories names to create in working directory by default .
    :return: None if found an exception
    """
    try:
        project_dir = getcwd()
        if len(dir_names) == 1:
            dirs_creator(dir_names[0])
        else:
            custom_path = input('Want to specify a certain path other than current directory [y/n] - ')
            if custom_path.lower().strip() == 'y':
                custom_path = input('Enter the path - ')
                while not exists(custom_path):
                    print('ERROR! Pls enter a existing path!')
                    custom_path = input('Enter the path - ')
                chdir(r'{}'.format(custom_path))
                makedirs(path_string(len(dir_names)).format(*dir_names))
                chdir(r'{}'.format(project_dir))
            else:
                makedirs(path_string(len(dir_names)).format(*dir_names))
    except FileExistsError:
        print('Directory/Directories {} already exists'.format(
            [dup for dup in dir_names if isdir(r'{}/{}'.format(getcwd(), dup))]))
        return None
    except Exception as error_msg:
        print('Exception in creating your specified directory is {}'.format(error_msg))
        return None
    finally:
        try:
            project_dir = getcwd()
            chdir(r'{}'.format(project_dir))
        except NameError as error_msg:
            print('NameError {}'.format(error_msg))
            return None
'''
'''
import csv
import time

# Generate a sample CSV file with 11,000 lines
input_csv_path = "/home/sahil/ai_nexus_classes/Assignments/OS_FileMove_Assignment/OS_FileMove_Assignment/source/business-operations-survey-2023-business-practices.csv"
output_csv_path = "sample_output.csv"

# Create a sample input CSV file

# Measure the time to read and write the CSV file
start_time = time.time()

with open(input_csv_path, 'r', encoding='latin-1') as infile, open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        writer.writerow(row)

end_time = time.time()

execution_time = end_time - start_time
print(execution_time)
''''''
import csv
def h(func):
    with open('/home/sahil/ai_nexus_classes/Assignments/OS_FileMove_Assignment/OS_FileMove_Assignment/source/business-financial-data-june-2024-quarter-csv.csv') as fp:
        data = csv.DictReader(fp)
        b , *a = data
        print(b)
        with open('testing.csv', 'w') as fp:
            w_obj = csv.DictWriter(fp, fieldnames=list(b.keys()))
            w_obj.writeheader()
            w_obj.writerow(b)
            w_obj.writerows(a)

def e(d):
    pass
h(e)
'''
def f(fp):
    print(fp.closed , fp.name)
    print(fp.read())
    print(fp.closed)

def m():
    with open('/home/sahil/ai_nexus_classes/Assignments/File_read_assignment/palin_test.txt') as fp:
        f(fp)
        print(fp.closed)
    print(fp.closed)


m()
