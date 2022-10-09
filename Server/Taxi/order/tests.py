from django.test import TestCase
import requests
# Create your tests here.

response = requests.post('http://127.0.0.1:8000/order', data = {
                                                                "id_user": 1,
                                                                "address_start": "улица Фёдора Лыткина Томск",
                                                                "address_end": "улица Горького 12 Мыски",
                                                                "ordered_time": "22:00",
                                                                "tariff": "comfort",
                                                                "payment": "MirPay",
                                                                "wishes": "Маленький ребёнок"
                                                                })
print(response.text)