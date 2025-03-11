import urllib.request
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://covid.ourworldindata.org/data/jhu/full_data.csv"
filename = "full_data.csv"

urllib.request.urlretrieve(url, filename)
print("Plik został pobrany i zapisany jako ", filename)

locations = set()
with open("full_data.csv") as datafile:
    for line in datafile:
        data = line.split(',')
        locations.add(data[1])
locations.remove('location') # usuwamy nagłówek (pierwszą linijkę pliku)
print('Available locations: ' , sorted(locations))
location_str = input('Choose a location: \n')

if location_str in locations:

    cases = {}

    with open("full_data.csv") as datafile:
        for line in datafile:
            data = line.split(',')
            if data[1] == location_str:
                if not data[2] == '': # niektóre wiersze mają "puste" dane - pozbywamy się ich
                    cases[data[0]] = float(data[2])

    dates = list(cases.keys())
    num_cases = list(cases.values())
    date_obj = [datetime.strptime(date, "%Y-%m-%d") for date in dates]
    plt.plot(date_obj,num_cases)
    plt.gcf().autofmt_xdate()  # obrócenie napisów na osi x dla większej czytelności
    plt.xlabel("date")
    plt.ylabel("number of new cases")
    plt.show()

else:
    print('Invalid location')
