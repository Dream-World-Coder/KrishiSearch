import os
import shutil

os.chdir(os.path.join(os.getcwd(), 'api'))

csv_directory = os.path.join(os.getcwd(), 'csv_files')
for file in os.listdir():
    if file.endswith('.csv'):
        shutil.move(file, csv_directory)


exceptions = ['all_states.html', 'wb_dist.html']
for file in os.listdir():
    if file not in exceptions and file.endswith('.html'):
        # os.remove(file)
        pass