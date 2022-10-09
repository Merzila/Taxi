from django.test import TestCase
import requests
# Create your tests here.

response = requests.get("http://127.0.0.1:8000/56.452513,84.974931,53.712258,87.801965")
print(response.text)