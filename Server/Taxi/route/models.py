from django.db import models

# Create your models here.

class Route(models.Model):

    route = models.TextField('Маршрут')
    coordinate_start = models.CharField('Начальные координаты', max_length = 100)
    coordinate_end = models.CharField('Конечные координаты', max_length = 100)
    address_start = models.CharField('Начальный адрес', max_length = 100)
    address_end = models.CharField('Конечный адрес', max_length = 100)
    distance = models.IntegerField('Дистанция, км')
    map = models.TextField('Карта, html')