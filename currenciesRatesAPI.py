import requests

currency_list = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON',
'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR',
'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS',
'KRW', 'PLN']

while True:
    base_currency = input('Enter base:')
    control_variable = 0
    for currency in range(len(currency_list)):
        if base_currency == currency_list[currency]:
            control_variable += 1
    if control_variable == 1:
        break

#Finish it later!!!!
def print_exchange_rate(base_currency):
    print('USD to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['USD'],2))


API_url = ('https://api.exchangeratesapi.io/latest?base=' + base_currency)

r = requests.get(API_url)
#Verifies if app works, if status code == 200 everything is great
print('Status code:', r.status_code)

#Stores API response as json
response_dictionary = r.json()
print('Update date:', response_dictionary['date'])
print('Base currency:', response_dictionary['base'])

rates_dictionary = response_dictionary['rates']

#Test if converts properly PLN to PLN, should return 1
#print(rates_dictionary['PLN'])


print('\n')
print('USD to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['USD'],2))
print('EUR to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['EUR'],2))
print('GBP to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['GBP'],2))
print('PLN to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['PLN'],2))
print('JPY to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['JPY'],2))
print('RUB to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['RUB'],2))

print_exchange_rate(base_currency)
