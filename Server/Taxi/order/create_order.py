import datetime
from route.getroute import get_distance
from .models import Order

def create_order(id_user, address_start, address_end, ordered_time, tariff, payment, wishes, coordinates, id_taxist = None):
    
    distance = float(get_distance(coordinates[0], coordinates[1], coordinates[2], coordinates[3]))

    if tariff == 'economy':
        coefficient = 1.5
    elif tariff == 'comfort':
        coefficient = 2.5
    else:
        coefficient = 5


    order = Order.objects.create(
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
                        cost = distance * coefficient * 20
                        )