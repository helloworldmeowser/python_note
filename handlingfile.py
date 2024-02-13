#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list
employee_list = read_employees('/home/student-04-a92fd1e10b35/data/employees.csv')
print(employee_list)


def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data
dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f: #To open a file for reading or writing, use open(filename, mode). 
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
write_report(dictionary, '/home/student-04-a92fd1e10b35/data/report.txt')

# To read and write a file, use Open() means returns a file object which is assigned to the variable file
# Readline() means reads one line from the files and returns it as a string
# Read() means reads the entire file and returns it as a string
# Close() means closes the file

#os.path.getsize("spider.txt")
#This code will provide the file size
#os.path.getmtime("spider.txt")
#This code will provide a timestamp for the file
#import datetime
#timestamp = os.path.getmtime("spider.txt")
#datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an easy too understand format
# os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path
