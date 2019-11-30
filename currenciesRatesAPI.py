import requests

def currency_variable_assign():
    currency_list = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON',
    'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR',
    'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS',
    'KRW', 'PLN']

    while True:
        user_currency = input('Enter base:')
        control_variable = False
        for currency in range(len(currency_list)):
            if user_currency == currency_list[currency]:
                control_variable = True
        if control_variable == True:
            return user_currency
            break

#Finish it later!!!!
def print_exchange_rate(base_currency, exchange_currency):
    print('%s' % base_currency + ' to %s exchange rate:' % exchange_currency, "%.2f" % round(1/rates_dictionary['%s' % exchange_currency],2))

base_currency = currency_variable_assign()
print(base_currency)

exchange_currency = currency_variable_assign()
print(exchange_currency)

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

"""
print('\n')
print('USD to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['USD'],2))
print('EUR to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['EUR'],2))
print('GBP to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['GBP'],2))
print('PLN to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['PLN'],2))
print('JPY to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['JPY'],2))
print('RUB to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['RUB'],2))
"""

print_exchange_rate(base_currency, exchange_currency)
