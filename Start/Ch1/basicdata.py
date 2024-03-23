# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?

max_temps = [day["tmax"] for day in weatherdata]
# print(max(max_temps))
print([day['date'] for day in weatherdata if day['tmax'] == 102])
# TODO: What was the coldest day in the data set?
min_temps = [day["tmin"] for day in weatherdata]
# print(min(min_temps))
print([day['date'] for day in weatherdata if day['tmin'] == min(min_temps)])

# TODO: How many days had snowfall?
snow_days = [day['date'] for day in weatherdata if day['snow'] != 0.0]
print(len(snow_days))