from django.test import TestCase
import requests
# Create your tests here.

def test_of_create_order():

    # Тестирование создания заказа

    response = requests.post('http://127.0.0.1:8000/order', data = {
                                                                    "id_user": 1,
                                                                    "address_start": "улица Фёдора Лыткина 8 Томск",
                                                                    "address_end": "улица Горького 12 Мыски",
                                                                    "ordered_time": "22:00",
                                                                    "tariff": "comfort",
                                                                    "payment": "MirPay",
                                                                    "wishes": "Маленький ребёнок"
                                                                    })

    id_order = response.json()['id_order']
    print(id_order)
    return id_order


def test_of_expectation(id_order):

    # Тестирование ожидания(поиска) таксиста

    response = requests.get('http://127.0.0.1:8000/order/expectation', params = {"id_order": id_order})
    print(response.text)


def response_to_expectation():

    # Тестирование отклика на заказ

    response = requests.post('http://127.0.0.1:8000/order/response', data = {'id_order': 1, 'id_taxist': 1})
    print(response.text)



id_order = test_of_create_order()
test_of_expectation(id_order)