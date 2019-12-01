import requests

#Function used to assign currency variables and to verify if they are compatibile with the API
def currency_variable_assign():
    currency_list = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON',
    'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR',
    'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS',
    'KRW', 'PLN']

    while True:
        user_currency = input('Input currency abbreviation:')
        control_variable = False
        for currency in range(len(currency_list)):
            if user_currency == currency_list[currency]:
                control_variable = True
        if control_variable == True:
            return user_currency
            break
        else:
            print('Unknown currency abbraviation, enter once again!')

#Function which allow to choose what user want to print
def print_exchange_rate(base_currency, exchange_currency):
    while True:
        #Necesesary line to access API rates and print exchange rates
        rates_dictionary = response_dictionary['rates']

        user_decision = input('Select 1 to see most popular currency exchange rates.\nSelect 2 to exchange chosen currencies.\nSelect q to quit.\nType your choice: ')
        if user_decision == 'q':
            break
        #This choice prints mos popular currency exchange rates
        elif user_decision == '1':
            print('\nUSD to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['USD'],2))
            print('EUR to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['EUR'],2))
            print('GBP to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['GBP'],2))
            print('PLN to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['PLN'],2))
            print('JPY to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['JPY'],2))
            print('RUB to %s exchange rate:' % base_currency, "%.2f" % round(1/rates_dictionary['RUB'],2))
        #Prints chosen currency exchange rate
        elif user_decision == '2':
            print('\n%s' % base_currency + ' to %s exchange rate:' % exchange_currency, "%.2f" % round(1/rates_dictionary['%s' % exchange_currency],2))
        else:
            print('\nUnknown command, select once again')

base_currency = currency_variable_assign()
exchange_currency = currency_variable_assign()

#API url, base_currency at the end is used to define base for the API
API_url = ('https://api.exchangeratesapi.io/latest?base=' + base_currency)

r = requests.get(API_url)

#Stores API response as json
response_dictionary = r.json()
print('Update date:', response_dictionary['date'])

print_exchange_rate(base_currency, exchange_currency)
