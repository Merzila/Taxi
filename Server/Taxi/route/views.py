from django.shortcuts import render
from django.http import JsonResponse
from .create_route import create_route

def showmap(request):
    # Показ карты без маршрута
    return render(request,'show_route/showmap.html')


def showroute(request, lat1, long1, lat2, long2):

    # Представление маршрута

    route = create_route(lat1, long1, lat2, long2)
    route.save()

    data = {
            "map": route.map,
            "id_route": route.pk,
            "economy": round(route.distance * 1.5 * 20),
            "comfort": round(route.distance * 2.5 * 20),
            "buisness": round(route.distance * 5 * 20),
            "address1": route.address_start,
            "address2": route.address_end
            }

    return JsonResponse(data)