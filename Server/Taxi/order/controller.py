import datetime
from .models import Order
from route.models import Route
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from autorization.models import Client

# Работа с закзом

def create_object_of_order(id_client, id_route, ordered_time, tariff, payment, wishes, id_taxist = None):
    
    # Создание экземпляра класса 'Заказ'

    route = Route.objects.get(pk = id_route)
    distance = route.distance
    map = route.map

    if tariff == 'economy':
        coefficient = 1.5
    elif tariff == 'comfort':
        coefficient = 2.5
    else:
        coefficient = 5


    order = Order(
                    id_client = id_client,
                    id_taxist = id_taxist,
                    address_start = route.address_start,
                    address_end = route.address_end,
                    ordered_time = ordered_time,
                    tariff = tariff,
                    payment = payment,
                    wishes = wishes,
                    time_of_order = str(datetime.datetime.now())[:-7],
                    distance = distance,
                    cost = distance * coefficient * 20,
                    status = 'expectation',
                    map = map
                )

    return order


@csrf_exempt
def order_response(request):

    # Отклик таксиста на заказ

    id_order = int(request.POST.get('id_order', ''))
    id_taxist = int(request.POST.get('id_taxist', ''))
    action = request.POST.get('action', '')

    order = Order.objects.get(pk = id_order)
    order.status = f'{action}'
    order.id_taxist = id_taxist
    order.save()

    if action == 'completed':
        client = Client.objects.get(pk = order.id_client)
        client.active_order = None
        client.save()

    return HttpResponse(action)
    

def cancel_of_order(request):

    # Отмена заказа пользователем

    id_client = int(request.POST.get('id_client', ''))

    client = Client.objects.get(pk = id_client)
    
    order = Order.objects.get(pk = client.active_order.pk)
    order.status = 'canceled'
    order.save()

    client.active_order = None
    client.save()

    return HttpResponse('OK')