from django.test import TestCase
import requests
# Create your tests here.

def test_of_create_order():

    # Тестирование создания заказа

    response = requests.post('http://127.0.0.1:8000/order', data = {
                                                                    "id_client": 1,
                                                                    "id_route": 2,
                                                                    "ordered_time": "22:00",
                                                                    "tariff": "comfort",
                                                                    "payment": "MirPay",
                                                                    "wishes": "Маленький ребёнок"
                                                                    })

    print(response.text)


def test_order_response():

    # Тестирование отклика таксиста на заказ

    response = requests.post('http://127.0.0.1:8000/order/response', data = {
                                                                            'id_taxist': 1,
                                                                            'id_order': 1,
                                                                            'action': 'completed'
                                                                            })

    print(response.text)

def test_cancel_of_order():

    # Тестирование отмены заказа

    response = requests.post('http://127.0.0.1:8000/order/cancel', data = {'id_client': 1})
    print(response.text)
    

test_cancel_of_order()