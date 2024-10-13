from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import selenium
import time
import json
import os


os.chdir(os.path.join(os.getcwd(), 'api'))


file_path = 'html/states_and_districts/all_states.html'
state_valut_list = []

with open(file_path, 'r') as f:
    string = f.read()

soup = BeautifulSoup(string, 'html.parser')
options = soup.find_all('option')
for option in options:
    if option.text != '--Select--':
        state_valut_list.append(option.text)

print(state_valut_list)


state_district_market_map = {}


url = "https://agmarknet.gov.in/"
output_file = 'markets_map.json'

driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(2)
time.sleep(3)


for state in state_valut_list:
    state_option = driver.find_element(By.XPATH, value='//*[@id="ddlState"]')
    select = Select(state_option)
    select.select_by_visible_text(state)

    time.sleep(1)


    district_option = driver.find_element(By.XPATH, value='//*[@id="ddlDistrict"]')
    select = Select(district_option)
    district_list = [opt.text for opt in select.options if opt.text != '--Select--']

    state_district_market_map[state] = {}


    for district in district_list:
        try:
            district_option = driver.find_element(By.XPATH, value='//*[@id="ddlDistrict"]')
            select = Select(district_option)
            select.select_by_visible_text(district)  # Select district by name

            time.sleep(1)

            market_option = driver.find_element(By.XPATH, value='//*[@id="ddlMarket"]')
            select_market = Select(market_option)
            market_list = [opt.text for opt in select_market.options if opt.text != '--Select--']

            state_district_market_map[state][district] = market_list

        except selenium.common.exceptions.StaleElementReferenceException:
            print(f"Stale element encountered when processing state: {state}, district: {district}. Retrying...")
            driver.refresh()
            time.sleep(1)
            district_option = driver.find_element(By.XPATH, value='//*[@id="ddlDistrict"]')
            select = Select(district_option)
            select.select_by_visible_text(district)

            market_option = driver.find_element(By.XPATH, value='//*[@id="ddlMarket"]')
            select_market = Select(market_option)
            market_list = [opt.text for opt in select_market.options if opt.text != '--Select--']

            state_district_market_map[state][district] = market_list

    print(f"Completed mapping for state: {state}")

driver.quit()

with open(output_file, 'w') as json_file:
    json.dump(state_district_market_map, json_file, indent=4)

print(f"Mapping completed and saved to {output_file}")
