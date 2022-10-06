from django.http import HttpResponse
import sqlite3, json
from route.getroute import coordinate_converter

def order(requests, id_user, time, ordered_time, tariff, payment, wishes):

    with open('route.json', 'r') as f:
            route = json.load(f)
            start = str(route['start_point'][0]) + ', ' + str(route['start_point'][1])
            end = str(route['end_point'][0]) + ', ' + str(route['end_point'][1])
            distance = str(round(float(route['distance'])/1000, 3))
    address1 = coordinate_converter(start)
    address2 = coordinate_converter(end)

    print(id_user, time, address1, address2, ordered_time, tariff, payment, wishes, distance)

    #with sqlite3.connect('db.sqlite3') as db:
    #    sql = db.cursor()
    #    sql.execute(f'INSERT INTO order_order VALUES ({id_user}, {id_taxist}, {time}, {address1},'+
    #                f'{address2}, {ordered_time}, {tariff}, {payment}, {wishes}, {distance}, {cost})')
    #    db.commit()

    return HttpResponse('OK')