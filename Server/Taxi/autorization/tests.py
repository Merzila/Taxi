from django.test import TestCase
import requests

# Create your tests here.

response = requests.post("http://127.0.0.1:8000/registration", data = {
                                                                        "user": "Users",
                                                                        "phone": "81234567890",
                                                                        "name": "admin",
                                                                        "password": "admin"
                                                                    })
print(response.text)

response = requests.post("http://127.0.0.1:8000/autorization", data = {
                                                                        "user": "Users",
                                                                        "phone": "81234567890",
                                                                        "password": "admin"
                                                                    })
print(response.text)
