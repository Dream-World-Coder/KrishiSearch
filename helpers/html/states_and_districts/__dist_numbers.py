import os 
import shutil
from collections import defaultdict
import csv


os.chdir(os.path.join(os.getcwd(), 'helpers/html/states_and_districts'))

csv_files_directory = 'csv_files'
output_file_path = 'district_numbers.csv'

# read all csv files in the 'csv_files_directory', 
# each csv files contain 2 columns and many rows. 
# the first column has a district name and 2nd one has its corresponding value
# but if you go through all  the files there you will realise that many districts have same number. 
# so you make abother csv 'output.csv' , and list the districts with same numbers with one row
# the first column will have the number and others will have the districts with same numbers
# suppose dist1 & dist2 both have number 3 , so in csv their mapping will be like that 3 - dist1 -dist2 etc.

# AND ITS NOT NECESSARY TO MAKE A CSV, JUST MAKE A FILE FROM WHERE VALUE CAN BE ACCESSED EASILY AND FAST 




districts_by_number = defaultdict(list)

for csv_file in os.listdir(csv_files_directory):
    if csv_file.endswith('.csv'):
        file_path = os.path.join(csv_files_directory, csv_file)
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:  # Ensure the row has exactly 2 columns
                    district, number = row
                    districts_by_number[number].append(district)

# Write the result to the output file
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for number, districts in districts_by_number.items():
        writer.writerow([number] + districts)

print(f'Successfully created {output_file_path}')
