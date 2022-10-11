from django.test import TestCase
import requests
# Create your tests here.

def test_of_create_order():
    response = requests.post('http://127.0.0.1:8000/order', data = {
                                                                    "id_user": 1,
                                                                    "address_start": "улица Фёдора Лыткина 8 Томск",
                                                                    "address_end": "улица Горького 12 Мыски",
                                                                    "ordered_time": "22:00",
                                                                    "tariff": "comfort",
                                                                    "payment": "MirPay",
                                                                    "wishes": "Маленький ребёнок"
                                                                    })
    print(response.text)

def test_of_expectation():
    response = requests.get('http://127.0.0.1:8000/order/expectation', params = {"id_order": 11})
    print(response.text)

def response_to_expectation():
    response = requests.post('http://127.0.0.1:8000/order/response', data = {'id_order': 7})

test_of_create_order()
test_of_expectation()