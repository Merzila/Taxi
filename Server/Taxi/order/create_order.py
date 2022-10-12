import datetime
from .models import Order
from route.models import Route

# Cоздание заказа

def create_order(id_user, id_route, address_start, address_end, ordered_time, tariff, payment, wishes, id_taxist = None):
    
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
                    id_user = id_user,
                    id_taxist = id_taxist,
                    address_start = address_start,
                    address_end = address_end,
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