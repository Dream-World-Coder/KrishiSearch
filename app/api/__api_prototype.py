import os
import csv
import json

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


os.chdir(os.path.join(os.getcwd(), 'api'))


urls = {
    'home':'https://agmarknet.gov.in/',
    
    'search1':
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=WB&Tx_District=2&Tx_Market=835&DateFrom=14-Aug-2024&DateTo=17-Aug-2024&Fr_Date=14-Aug-2024&To_Date=17-Aug-2024&Tx_Trend=2&Tx_CommodityHead=Onion&Tx_StateHead=West+Bengal&Tx_DistrictHead=Bankura&Tx_MarketHead=Bishnupur(Bankura)',
        
    'pricetrend':
        'https://agmarknet.gov.in/PriceTrends/SA_Pri_MonthRep.aspx', # post req i think
}


# with open("helpers/node.html") as f:
#     string:str = f.read()
# soup = BeautifulSoup(string, 'html.parser')

items_dict = {'id':'name'}

# options_list = soup.find_all('option')
# for option in options_list:
#     # key = f'no_{option.attrs.get('value')}'
#     key = int(option.attrs.get('value'))
    
#     value = option.text
#     items_dict[key] = value




comodity_id = 23, # listing done
state_name_SN = 'WB' # listing undone
district_serial = 2 # can vary , based on alphabeticla words, need to take a look at all states
market_id = 835
d = 7
Mmm = 'Aug'
yyyy = 2024
d2 = 7
Mmm2 = 'Aug'
tx_trend = 2
# api_url = f"{urls["home"]}SearchCmmMkt.aspx?Tx_Commodity={comodity_id}&Tx_State={state_name_SN}&Tx_District={district_serial}&Tx_Market={market_id}&DateFrom={d}-{Mmm}-{yyyy}&DateTo={d2}-{Mmm2}-{yyyy}&Fr_Date={d}-{Mmm}-{yyyy}&To_Date={14}-{Mmm}-{yyyy}&Tx_Trend={tx_trend}&Tx_CommodityHead={items_dict['no_{comodity_id}']}&Tx_StateHead={'West'}+{'Bengal'}&Tx_DistrictHead={'Bankura'}&Tx_MarketHead={'Bishnupur(Bankura)'}"



# check the last update etc

def get_commodity_id_from_name(p):
    pass
def get_state_code_from_name(p):
    pass
def get_district_id_from_name(p):
    pass
def get_market_id_from_name(p):
    pass
def get_commodity_id_from_name2(commodity_name, csv_file_path):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['commodity name'].strip().lower() == commodity_name.strip().lower():
                return row['id']
    
    # If commodity name is not found
    return None

# normally je district ta add kora thakbe login e setar sob market gulor price dekha jabe
# unless very specific [upto the market], only upto district level prices will be shown
# like if choose state >> select dist



base_url = 'https://agmarknet.gov.in/'

commodity = 'Rice'
comodity_id = get_commodity_id_from_name(commodity)

state = 'west bengal'
state_code = get_state_code_from_name(state)

district = 'bankura'
district_id = get_district_id_from_name(district)

market = 'bishnupur' # or '*'
market_id = get_market_id_from_name(market)

date_from = 'd-Mmm-yyyy'
dtae_to = ''

tx_trend = 0 # or 2[both]

api_dict = {
    'queries' : {
        
    },
}


url = urls['search1']
res = requests.post(url=url, timeout=10, allow_redirects=True)


with open('response.html', 'wb') as f:
    f.write(res.content)
# faster

with open('response.html', 'r') as f:
    content = f.read()
print(content)
# print(res.content.decode('utf-8'))
soup = BeautifulSoup(content, 'html.parser')
rows = soup.find('table', id='cphBody_GridViewBoth', class_='tableagmark_new').find_all('tr')


header_list = rows[0].find_all('th')
h_lst = []
middles = rows[1:-2]
d_lst = []
total = rows[-2:]  # index : 4,5 [val exits]
t_lst = []


with open('response.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    for h in header_list:
        h_lst.append(h.text)
    writer.writerow(h_lst)
    
    for middle in middles:
        data = middle.find_all('td')
        for d in data:
            d_lst.append(d.text)
        writer.writerow(d_lst)
        d_lst = []
    
    for t in total:
        data = t.find_all('td')
        for d in data:
            t_lst.append(d.text)
        writer.writerow(t_lst)
        t_lst = []