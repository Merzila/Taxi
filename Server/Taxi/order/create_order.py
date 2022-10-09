from django.http import HttpResponse
import sqlite3, datetime
from route.getroute import get_distance, address_converter
from django.views.decorators.csrf import csrf_exempt
from route.views import get_map

@csrf_exempt
def order(request):

    id_user = request.POST.get('id_user', '')
    address_start = request.POST.get('address_start', '')
    address_end = request.POST.get('address_end', '')
    ordered_time = request.POST.get('ordered_time', '')
    tariff = request.POST.get('tariff', '')
    payment = request.POST.get('payment', '')
    wishes = request.POST.get('wishes', '')

    time_of_order = str(datetime.datetime.now())[:-7]
    coordinates = address_converter(address_start, address_end).split(",")
    distance = get_distance(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    
    print(id_user, ordered_time, address_start, address_end, distance, time_of_order, tariff, payment, wishes)
    
    #with sqlite3.connect('db.sqlite3') as db:
    #    sql = db.cursor()
    #    sql.execute(f'INSERT INTO order_order VALUES ({id_user}, {id_taxist}, {time}, {address1},'+
    #                f'{address2}, {ordered_time}, {tariff}, {payment}, {wishes}, {distance}, {cost})')
    #    db.commit()

    map = get_map(request, coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    
    return HttpResponse(map)