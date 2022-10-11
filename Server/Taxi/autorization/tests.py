from django.test import TestCase
import requests

# Create your tests here.
# Тестирование регистрации и авторизации пользователя

def test_reg(user, phone, name, password):

    response = requests.post("http://127.0.0.1:8000/registration", data = {
                                                                            "user": user,
                                                                            "phone": phone,
                                                                            "name": name,
                                                                            "password": password
                                                                        })
    print(response.text)


def test_login(user, phone, password):

    response = requests.post("http://127.0.0.1:8000/autorization", data = {
                                                                            "user": user,
                                                                            "phone": phone,
                                                                            "password": password
                                                                        })
    print(response.text)

test_reg("User", "81234567890", "admin", "admin")
test_login("User", "81234567890", "admin")