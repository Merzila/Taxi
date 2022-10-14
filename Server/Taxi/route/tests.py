from django.test import TestCase
import requests
# Create your tests here.
# Тестирование построения маршрута и возврата карты с маршрутом

def test_of_create_order_with_coordinate():

    data = {
            'lat1': '56.452513',
            'long1': '84.974931',
            'lat2': '53.712258',
            'long2': '87.801965'
            }

    response = requests.get("http://127.0.0.1:8000/route", params = data)
    print(response.text)


def test_of_create_order_with_addresses():

    data = {
            'address_start': 'улица Фёдора Лыткина 8 Томск',
            'address_end': 'улица Горького 12 Мыски'
            }

    response = requests.get("http://127.0.0.1:8000/route", params = data)
    print(response.text)

test_of_create_order_with_addresses()