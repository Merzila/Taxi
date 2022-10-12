from .models import Route
from route import getroute

def create_route(lat1, long1, lat2, long2):

    address_start = getroute.get_address(lat1, long1)
    address_end = getroute.get_address(lat2, long2)
    route = getroute.get_route(lat1,long1,lat2,long2)
    map = getroute.get_map(lat1, long1, lat2, long2, route)

    route = Route(route = route['route'],
                  coordinate_start = route['start_point'],
                  coordinate_end = route['end_point'],
                  distance = route['distance'],
                  address_start = address_start,
                  address_end = address_end,
                  map = map)

    return route