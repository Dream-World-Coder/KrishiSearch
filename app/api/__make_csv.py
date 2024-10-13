from bs4 import BeautifulSoup
import csv
import os


os.chdir(os.path.join(os.getcwd(), 'api'))

# commodities.csv
source_file = 'html/commodities.html'
output_file = 'csvs/commodities.csv'

with open(source_file, 'r') as f:
    string = f.read()

soup = BeautifulSoup(string, 'html.parser')
options = soup.find_all('option')

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for option in options:
        writer.writerow([option.text, option['value']])
print(f"Successfully created {output_file}")







# states_code.csv
source_file = 'html/states.html'
output_file = 'csvs/states_code.csv'

with open(source_file, 'r') as f:
    string = f.read()

soup = BeautifulSoup(string, 'html.parser')
options = soup.find_all('option')

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for option in options:
        writer.writerow([option.text, option['value']])
print(f"Successfully created {output_file}")








# districts_id.csv
# Already Exists





# markets_id.csv
source_file = 'html/markets.html'
output_file = 'csvs/markets_id.csv'

with open(source_file, 'r') as f:
    string = f.read()

soup = BeautifulSoup(string, 'html.parser')
options = soup.find_all('option')

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for option in options:
        writer.writerow([option.text, option['value']])
print(f"Successfully created {output_file}")
