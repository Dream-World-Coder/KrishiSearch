import requests
import urllib
import utils.scraper
import utils.csv_maker
import utils.decorators
import json
from bs4 import BeautifulSoup
import csv

urls = {
    'home':'https://agmarknet.gov.in/',
    
    'search1':
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=WB&Tx_District=2&Tx_Market=835&DateFrom=7-Aug-2024&DateTo=14-Aug-2024&Fr_Date=7-Aug-2024&To_Date=14-Aug-2024&Tx_Trend=2&Tx_CommodityHead=Onion&Tx_StateHead=West+Bengal&Tx_DistrictHead=Bankura&Tx_MarketHead=Bishnupur(Bankura)',
        
    'search2':
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=17&Tx_State=WB&Tx_District=18&Tx_Market=2639&DateFrom=10-Aug-2024&DateTo=14-Aug-2024&Fr_Date=10-Aug-2024&To_Date=14-Aug-2024&Tx_Trend=2&Tx_CommodityHead=Apple&Tx_StateHead=West+Bengal&Tx_DistrictHead=Howrah&Tx_MarketHead=Howrah', # no results
    
    'search3': 
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=19&Tx_State=WB&Tx_District=2&Tx_Market=835&DateFrom=1-Aug-2024&DateTo=08-Aug-2024&Fr_Date=1-Aug-2024&To_Date=08-Aug-2024&Tx_Trend=0&Tx_CommodityHead=Banana&Tx_StateHead=West+Bengal&Tx_DistrictHead=Bankura&Tx_MarketHead=Bishnupur(Bankura)',
        
    'search4':
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=WB&Tx_District=2&Tx_Market=835&DateFrom=1-Aug-2024&DateTo=08-Aug-2024&Fr_Date=1-Aug-2024&To_Date=08-Aug-2024&Tx_Trend=0&Tx_CommodityHead=Onion&Tx_StateHead=West+Bengal&Tx_DistrictHead=Bankura&Tx_MarketHead=Bishnupur(Bankura)', #res
        
    'search5':
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=451&Tx_State=AN&Tx_District=2&Tx_Market=0&DateFrom=1-Aug-2024&DateTo=08-Aug-2024&Fr_Date=1-Aug-2024&To_Date=08-Aug-2024&Tx_Trend=0&Tx_CommodityHead=Absinthe&Tx_StateHead=Andaman+and+Nicobar&Tx_DistrictHead=Nicobar&Tx_MarketHead=--Select--',
        
    'search6': 
        'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=4&Tx_State=WB&Tx_District=16&Tx_Market=3625&DateFrom=04-Jun-2024&DateTo=02-Jul-2024&Fr_Date=04-Jun-2024&To_Date=02-Jul-2024&Tx_Trend=0&Tx_CommodityHead=Paddy(Dhan)(Common)&Tx_StateHead=West+Bengal&Tx_DistrictHead=Kolkata&Tx_MarketHead=Bara+Bazar+(Posta+Bazar)', # paddy normal id = 2
        
    'pricetrend':
        'https://agmarknet.gov.in/PriceTrends/SA_Pri_MonthRep.aspx', # post req i think
}


# res = requests.get(url=urls['search6'], timeout=10, allow_redirects=True)
# res.raise_for_status()
# print(res.content)

# with open("helpers/res.txt", 'w') as f:
    # f.write(str(res.content)) :- response is html page not json
    


with open("helpers/node.html") as f:
    string:str = f.read()
soup = BeautifulSoup(string, 'html.parser')

items_dict = {'id':'name'}

options_list = soup.find_all('option')
for option in options_list:
    # key = f'no_{option.attrs.get('value')}'
    key = int(option.attrs.get('value'))
    
    value = option.text
    items_dict[key] = value


# opt_lst = list(items_dict.keys())
# opt_lst.remove('id')
# opt_lst.sort()
# print(opt_lst)

# with open("helpers/sorted-data.txt", 'w') as f:
    # for key in opt_lst:
        # line = f'{key}, {items_dict[key]}'
        # f.write(line + '\n')

# csv_file = "helpers/options.csv"
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)

#     for key, value in items_dict.items():
#         writer.writerow([key, value])

# print(f"Data has been written to {csv_file}")




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

api_url = f"{urls["home"]}SearchCmmMkt.aspx?Tx_Commodity={comodity_id}&Tx_State={state_name_SN}&Tx_District={district_serial}&Tx_Market={market_id}&DateFrom={d}-{Mmm}-{yyyy}&DateTo={d2}-{Mmm2}-{yyyy}&Fr_Date={d}-{Mmm}-{yyyy}&To_Date={14}-{Mmm}-{yyyy}&Tx_Trend={tx_trend}&Tx_CommodityHead={items_dict['no_{comodity_id}']}&Tx_StateHead={'West'}+{'Bengal'}&Tx_DistrictHead={'Bankura'}&Tx_MarketHead={'Bishnupur(Bankura)'}"


# check the last update eyc.