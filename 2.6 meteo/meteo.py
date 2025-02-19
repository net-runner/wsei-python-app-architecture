import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import defaultdict

url = 'https://danepubliczne.imgw.pl/api/data/meteo/format/xml'
response = requests.get(url)
xml_data = response.content

root = ET.fromstring(xml_data)
selected_stations = ['KRAKÓW-BALICE', 'KRAKÓW-WOLA JUSTOWSKA', 'OBIDOWA', 'STRUSZEWO', 'ŚNIEŻNIK']

wind_speeds = defaultdict(list)

for station in root.findall('item'):
    station_name = station.find('nazwa_stacji').text
    if station_name in selected_stations:
        wind_speed_text = station.find('wiatr_srednia_predkosc').text
        if wind_speed_text is not None and wind_speed_text.strip():
            try:
                wind_speed = float(wind_speed_text.replace(',', '.'))
                wind_speeds[station_name].append(wind_speed)
            except ValueError:
                continue

average_wind_speeds = {}
for station_name, speeds in wind_speeds.items():
    if speeds:
        average = sum(speeds) / len(speeds)
        average_wind_speeds[station_name] = average
    else:
        average_wind_speeds[station_name] = 0

stations = list(average_wind_speeds.keys())
averages = [average_wind_speeds[station] for station in stations]

plt.figure(figsize=(10, 6))
plt.bar(stations, averages, color='skyblue')
plt.xlabel('Stacja')
plt.ylabel('Średnia prędkość wiatru [m/s]')
plt.title('Średnia prędkość wiatru na wybranych stacjach IMGW')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()