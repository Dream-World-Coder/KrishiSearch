from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import requests
import csv
import os

def make_csv(data: iter, output_file: str) -> None:
    try:
        transposed_data = list(zip(*data))
        
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(transposed_data)
        
        print(f'Successfully created {output_file}')

    except Exception as e:
        print(e)

        
# if opend in root directory
os.chdir(os.path.join(os.getcwd(), 'api'))

file_path = 'all_states.html'
state_valut_list = []

with open(file_path, 'r') as f:
    string = f.read()
    
soup = BeautifulSoup(string, 'html.parser')
options = soup.find_all('option')
for option in options:
    if option.text != '--Select--':
        # state_valut_list.append(option.attrs.get('value')) # by value
        state_valut_list.append(option.text) #by name

print(state_valut_list)



url = "https://agmarknet.gov.in/"
state_district_dictionary = {'state_name':['dist_list']}




driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)
driver.implicitly_wait(2)


for val in state_valut_list:
    element_to_select = driver.find_element(By.XPATH, value='//*[@id="ddlState"]')
    select = Select(element_to_select)
    # select.select_by_value(val) # by value
    select.select_by_visible_text(val) # by name
    
    time.sleep(2)
    driver.implicitly_wait(1.5)
    district_container = driver.find_element(By.XPATH, value='//*[@id="ddlDistrict"]')
    districts = district_container.find_elements(By.TAG_NAME, 'option')
    
    districts_list = []
    districts_value_list = []
    for dst in districts[1:]:
        district_name = dst.text
        districts_list.append(district_name)
        district_value = dst.get_attribute('value')
        districts_value_list.append(district_value)
    
    # the html of that node
    fname = f'{val}_districts.html'
    with open(fname, 'w') as f:
        f.write(district_container.get_attribute('outerHTML'))
    print(f"{fname} created successfully.")
    
    # csv of that node
    fname = f'{val}_districts.csv'
    make_csv(data=[districts_list, districts_value_list], output_file=fname)
        
    print(f"{fname} created successfully")    



driver.quit()