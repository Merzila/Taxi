from django.shortcuts import render
from .create_order import create_order
from route.getroute import address_converter
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from route.create_route import create_route

# Create your views here.

@csrf_exempt
def view(request):
    
    # Создание заказа и его запись в БД

    id_user = request.POST.get('id_user', '')
    id_route = request.POST.get('id_route', '')
    address_start = request.POST.get('address_start', '')
    address_end = request.POST.get('address_end', '')
    ordered_time = request.POST.get('ordered_time', '')
    tariff = request.POST.get('tariff', '')
    payment = request.POST.get('payment', '')
    wishes = request.POST.get('wishes', '')

    if id_route == '':
        coordinates = address_converter(address_start, address_end).split(",")
        route = create_route(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        route.save()
        id_route = route.pk

    order = create_order(id_user, id_route, address_start, address_end, ordered_time, tariff, payment, wishes)
    order.save()

    return JsonResponse({
                        "map": order.map,
                        "id_order": order.pk
                        })