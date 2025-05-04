import pandas as pd
import plotly
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
df = pd.read_csv('adjusted.csv')

loc = df['location']

lat = []
lon = []

geolocator = Nominatim(user_agent='geoapi', timeout=10)

def get_lat_lon(location, lat, lon):
    for k,v in location['location'].items():
        elem = v.split(',', 2)
        try:
            geo = geolocator.geocode(elem[1])
            if geo:
                print('passed')
                print(elem)
                lon.append(geo.longitude)
                lat.append(geo.latitude)
            else:
                print('useing elem2')
                print(elem)
                try:
                    geo = geolocator.geocode(elem[2])
                    lat.append(geo.longitude)
                    lon.append(geo.latitude)
                except AttributeError:
                    print('Couldnt find a location')
                    lat.append('None')
                    lon.append('None')  
                except IndexError:
                    print('index out of range')
                    lat.append('None')
                    lon.append('None')    
        except GeocoderTimedOut:
            time.sleep(1)

get_lat_lon(df, lat, lon)

print(lat)
print(lon)

df['latitude'] = lat
df['longitude'] = lon

df.to_csv('another-adjusted.csv', index=False)