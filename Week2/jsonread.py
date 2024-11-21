class WeatherData:
    def __init__(self, date, tmin, tmax, prcp, snow, snwd, awnd):
        self.date = date
        self.tmin = tmin
        self.tmax = tmax
        self.prcp = prcp
        self.snow = snow
        self.snwd = snwd
        self.awnd = awnd

    def __str__(self):
        return f'{self.date}: {self.tmin}/{self.tmax}'


import json

path = './../SourceData/rdu-weather-history.json'

with open (path, "r") as file:
    weatherdict = json.load(file)

print(type(weatherdict))
print(type(weatherdict[0]))

weatherobjs = []
for x in weatherdict:
    entry = WeatherData(x['date'], x['tmin'], x['tmax'], x['prcp'], x['snow'], x['snwd'], x['awnd'])
    weatherobjs.append(entry)

for i in weatherobjs:
    print(i)