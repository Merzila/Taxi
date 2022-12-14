from django.db import models
from order.models import Order
# Create your models here.


class Client(models.Model):

    phone = models.IntegerField('Номер телефона')
    name = models.CharField('Имя', max_length=50)
    password = models.BinaryField('Пароль')
    active_order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.phone


class Taxist(models.Model):

    phone = models.IntegerField('Номер телефона')
    name = models.CharField('Имя', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    model_of_car = models.CharField('Модель автомобиля', max_length=50)
    color_of_car = models.CharField('Цвет автомобиля', max_length=50)
    state_number = models.CharField('Номер автомобиля', max_length=9)
    

    def __str__(self):
        return self.phone