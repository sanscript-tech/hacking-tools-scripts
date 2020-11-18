import requests
api = "https://api.exchangerate-api.com/v4/latest/USD"
# Getting Currency Rates from the API
rates = requests.get(api).json()['rates']
# Currency from which we need to convert
from_currency = input("Enter the currency code from which you want to convert : ").upper()
# Currency to which we are converting
to_currency = input("Enter the currency code to which you want to convert : ").upper()
value = float(input("Enter the currency amount : "))
# Since the base in API is USD
# we will first convert value to usd and then result to the requested currency
try:
	from_currency_dollars = value/rates[from_currency]
	result = from_currency_dollars * rates[to_currency]
	result = round(result, 2)
	print(f"{value} {from_currency} is equivalent to {result} {to_currency}")
except KeyError:
	print("Check the currency codes you entered")