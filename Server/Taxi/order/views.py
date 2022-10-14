from django.shortcuts import render
from .controller import create_object_of_order
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from autorization.models import Client

# Create your views here.

@csrf_exempt
def create_order(request):
    
    # Создание заказа и его запись в БД

    id_client = request.POST.get('id_client', '')
    id_route = request.POST.get('id_route', '')
    ordered_time = request.POST.get('ordered_time', '')
    tariff = request.POST.get('tariff', '')
    payment = request.POST.get('payment', '')
    wishes = request.POST.get('wishes', '')

    order = create_object_of_order(id_client, id_route, ordered_time, tariff, payment, wishes)
    order.save()

    user = Client.objects.get(pk = id_client)
    user.active_order = order
    user.save()

    return HttpResponse(order.pk)