import requests
import json
import tkinter as tk
from tkinter import messagebox
import time

while True:
    url="https://api.covid19api.com/total/country/india"
    response = requests.request("GET", url)
    parsed_data = json.loads(response.text)
    Active_cases = parsed_data[-1]["Active"]
    Recovered = parsed_data[-1]["Recovered"]
    Deaths = parsed_data[-1]["Deaths"]
    root = tk.Tk()
    root.withdraw()
    final = "Active Cases :" + str(Active_cases) + "\n" + "Recovered :" + str(Recovered) + "\n" + "Deaths :" + str(Deaths)
    messagebox.showwarning('Covid Update for India', final)
    time.sleep(3600)
