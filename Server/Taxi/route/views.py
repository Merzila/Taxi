from django.shortcuts import render
import folium
from . import getroute
from django.http import JsonResponse
from django.template import loader
from .models import Route

def showmap(request):
    # Показ карты без маршрута
    return render(request,'show_route/showmap.html')


def showroute(request, lat1, long1, lat2, long2):

    # Представление маршрута

    address_start = getroute.get_address(lat1, long1)
    address_end = getroute.get_address(lat2, long2)
    route = getroute.get_route(lat1,long1,lat2,long2)
    map = get_map(lat1, long1, lat2, long2, route)

    Route.objects.create(route = route['route'],
                        coordinate_start = route['start_point'],
                        coordinate_end = route['end_point'],
                        distance = route['distance'],
                        address_start = address_start,
                        address_end = address_end,
                        map = map)

    data = {
            "map": map,
            "economy": round(route["distance"] * 1.5 * 20),
            "comfort": round(route["distance"] * 2.5 * 20),
            "buisness": round(route["distance"] * 5 * 20),
            "address1": address_start,
            "address2": address_end
            }

    return JsonResponse(data)


def get_map(lat1, long1, lat2, long2, route = None):

    # Получение карты с маршрутом

    figure = folium.Figure()
    lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)

    if route == None:
        route=getroute.get_route(lat1,long1,lat2,long2)
        
    m = folium.Map(location=[(route['start_point'][0]),
                                 (route['start_point'][1])], 
                       zoom_start=10)
    m.add_to(figure)
    folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
    folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
    folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
    figure.render()
    context={'map':figure}
    
    map = loader.render_to_string('show_route/showroute.html', context)

    return map