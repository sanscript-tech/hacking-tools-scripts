import csv
import requests

with open("IP_data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ip_address = row['IP']
        api_url = "http://ip-api.com/json/" + ip_address
        response = requests.get(api_url).json()

        city = response['city']
        state = response['regionName']
        country = response['country']

        print(f"{ip_address} => {city}, {state}, {country}")
