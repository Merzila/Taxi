from django.shortcuts import render
from .create_order import create_order
from route.getroute import address_converter
from route.views import get_map
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def view(request):

    id_user = request.POST.get('id_user', '')
    address_start = request.POST.get('address_start', '')
    address_end = request.POST.get('address_end', '')
    ordered_time = request.POST.get('ordered_time', '')
    tariff = request.POST.get('tariff', '')
    payment = request.POST.get('payment', '')
    wishes = request.POST.get('wishes', '')

    coordinates = address_converter(address_start, address_end).split(",")
    create_order(id_user, address_start, address_end, ordered_time, tariff, payment, wishes, coordinates)

    map = get_map(request, coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    
    return HttpResponse("OK")