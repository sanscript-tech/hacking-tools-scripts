import csv
import requests

# Create a context manager to open `.csv` file.
with open("IP_data.csv") as csvfile:
    # Create an iterator which iterates through the rows of the file
    # and returns the rows as dictionaries when invoked.
    reader = csv.DictReader(csvfile)

    # Iterate through the rows.
    for row in reader:
        # Get the IP address from the `IP` column.
        ip_address = row['IP']

        # Generate the IP URL and perform a GET request.
        api_url = "http://ip-api.com/json/" + ip_address
        response = requests.get(api_url).json()

        # extract important info to make code readable.
        city = response['city']
        state = response['regionName']
        country = response['country']

        # Print results to console output.
        print(f"{ip_address} => {city}, {state}, {country}")
