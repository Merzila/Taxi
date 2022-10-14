from django.shortcuts import render
from django.http import JsonResponse
from .controller import create_object_of_route, address_converter

def get_view_map(request):
    # Получение вида карты без маршрута
    return render(request,'show_route/showmap.html')


def get_view_route(request):

    # Создание маршрута
    # Получение вида карты с маршрутом

    lat1 = request.GET.get('lat1', '')
    if lat1 != '':
        long1 = request.GET.get('long1', '')
        lat2 = request.GET.get('lat2', '')
        long2 = request.GET.get('long2', '')
    else:
        address_start = request.GET.get('address_start')
        address_end = request.GET.get('address_end')
        lat1, long1 = address_converter(address_start).split(',')
        lat2, long2 = address_converter(address_end).split(',')

    route = create_object_of_route(lat1, long1, lat2, long2)
    route.save()

    data = {
            "map": route.map,
            "id_route": route.pk,
            "economy": round(route.distance * 1.5 * 20),
            "comfort": round(route.distance * 2.5 * 20),
            "buisness": round(route.distance * 5 * 20),
            "address_start": route.address_start,
            "address_end": route.address_end
            }

    return JsonResponse(data)