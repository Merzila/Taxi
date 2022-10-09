from tkinter import W
import requests
import json
import polyline
import folium
from geopy.geocoders import Nominatim
from django.http import HttpResponse
from geopy import Nominatim

def get_route(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon):
    loc = "{},{};{},{}".format(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc) 
    if r.status_code != 200:
        return {}
    res = r.json()   
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']
    
    out = {'route':routes,
           'start_point':start_point,
           'end_point':end_point,
           'distance':distance
          }
          
    with open('route.json', 'w') as f:
        json.dump(out, f)

    return out

def get_distance(lat1, long1, lat2, lon2):
    out = get_route(lat1, long1, lat2, lon2)
    return f'{out["distance"]}'

def address_converter(address1, address2):
    loc1 = Nominatim(user_agent='my_request').geocode(address1)
    loc2 = Nominatim(user_agent='my_request').geocode(address2)
    return f'{loc1.latitude},{loc1.longitude},{loc2.latitude},{loc2.longitude}'

def coordinate_converter(coordinates):
    naminaltim = Nominatim(user_agent = 'user')
    address = naminaltim.reverse(coordinates)
    return address

def get_address(lat1,long1):
    address = str(coordinate_converter(f"{lat1},{long1}")).split(", ")

    for i in range(10):
        try:
            address[i] = int(address[i])
            address = f"{address[i+1]} {address[i]}"
        except:
            pass

    return address