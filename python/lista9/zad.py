import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [11, 7]
plt.rcParams["figure.autolayout"] = True
fig,axs = plt.subplots(3, sharey=True)


def monthly_average(data, param1, param2):
    monthly_prices = defaultdict(list)

    for entry in data:
        date = entry[param1] #'data' or 'effectiveDate'
        price = entry[param2] #'cena' or 'mid'
        month = date[5:7]
        monthly_prices[month].append(price)

    monthly_averages = {}
    for month, prices in monthly_prices.items():
        average_price = sum(prices) / len(prices)
        monthly_averages[month] = round(average_price,4)

    return monthly_averages

def predictions(dict1, dict2):
    keys = list(dict1.keys())
    result = dict()

    for key in keys:
        result[key] = round((dict1[key] + dict2[key])/2,4)
    
    return result

def get_NBPgold(year):
    data = f'http://api.nbp.pl/api/cenyzlota/{year}-01-01/{year}-12-31/'
    response = requests.get(data)
    
    return json.loads(response.text)

def get_euro(year):
    data = f'http://api.nbp.pl/api/exchangerates/rates/A/EUR/{year}-01-01/{year}-12-31/'
    response = requests.get(data)
    
    return json.loads(response.text)['rates']


gold21 = monthly_average(get_NBPgold(2021), 'data', 'cena')
gold22 = monthly_average(get_NBPgold(2022), 'data', 'cena')

euro21 = monthly_average(get_euro(2021), 'effectiveDate', 'mid')
euro22 = monthly_average(get_euro(2021), 'effectiveDate', 'mid')

gold23_pred = predictions(gold21, gold22)
euro23_pred = predictions(euro21, euro22)

#-----------------------------------------------

#2021
axs[0].plot(list(gold21.keys()), list(gold21.values()), label='Gold 2021')
axs[0].plot(list(euro21.keys()), list(euro21.values()), label='Euro 2021')
axs[0].set_title('Gold and Euro Prices in 2021')
axs[0].legend()
axs[0].set(xlabel='Month', ylabel='[polish zloty]')

# 2022
axs[1].plot(list(gold22.keys()), list(gold22.values()), label='Gold 2022')
axs[1].plot(list(euro22.keys()), list(euro22.values()), label='Euro 2022')
axs[1].set_title('Gold and Euro Prices in 2022')
axs[1].legend()
axs[1].set(xlabel='Month', ylabel='[polish zloty]')

# 2023 - predictions
axs[2].plot(list(gold23_pred.keys()), list(gold23_pred.values()), label='Gold 2023 (Predicted)')
axs[2].plot(list(euro23_pred.keys()), list(euro23_pred.values()), label='Euro 2023 (Predicted)')
axs[2].set_title('Gold and Euro Prices Prediction for 2023')
axs[2].legend()
axs[2].set(xlabel='Month', ylabel='[polish zloty]')

plt.show()