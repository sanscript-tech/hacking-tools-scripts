#Imports and dependencies
import requests
import json

#Using the ip-api API, the geolocation coordinates are obtained
def get_location():
        IP_address = input("Enter your IP address ")
        URL = "http://ip-api.com/json/" + IP_address
        try:
            response = requests.get(URL)
            latitude = response.json()["lat"]
            longitude = response.json()["lon"]
            return(1, [latitude, longitude])
        except:
            return(0, "Location with that IP is non-existent")

if __name__ == "__main__":
    valid, response = get_location()
    if valid:
        print("The latitude is : ", end = "")
        print(response[0])
        print("The longitude is : ", end = "")
        print(response[1])
    else:
        print(response)


