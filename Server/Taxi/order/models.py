from django.db import models
from route.models import Route

# Create your models here.

class Order(models.Model):

    id_client = models.IntegerField('id заказчика')
    id_taxist = models.IntegerField('id таксиста', null = True)
    time_of_order = models.CharField('Время заказа', max_length = 50)
    ordered_time = models.CharField('Заказанное время', max_length = 50)
    tariff = models.CharField('Тариф', max_length = 50)
    payment = models.CharField('Оплата', max_length = 50)
    wishes = models.CharField('Пожелания', max_length = 50)
    cost = models.FloatField('Стоимость, руб')
    status = models.CharField('Статус', max_length = 15)
    route = models.ForeignKey(Route, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return str(self.pk)