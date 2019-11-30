import requests

API_url = 'https://api.exchangeratesapi.io/latest?base=PLN'

r = requests.get(API_url)
#Verifies if app works, if status code == 200 everything is great
print('Status code:', r.status_code)

#Stores API response as json
response_dictionary = r.json()
print('Update date:', response_dictionary['date'])
print('Base currency:', response_dictionary['base'])

rates_dictionary = response_dictionary['rates']
#print(rates_dictionary.keys())
"""RETURNS
dict_keys(['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON',
'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR',
'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS',
'KRW', 'PLN'])
"""
#Test if converts properly PLN to PLN, should return 1
#print(rates_dictionary['PLN'])

print('\n\n')
print('USD to PLN exchange rate:', "%.2f" % round(1/rates_dictionary['USD'],2))
print('EUR to PLN exchange rate:', "%.2f" % round(1/rates_dictionary['EUR'],2))
print('GBP to PLN exchange rate:', "%.2f" % round(1/rates_dictionary['GBP'],2))
print('JPY to PLN exchange rate:', "%.2f" % round(1/rates_dictionary['JPY'],2))
print('RUB to PLN exchange rate:', "%.2f" % round(1/rates_dictionary['RUB'],2))
