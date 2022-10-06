from django.db import models

# Create your models here.

class Order(models.Model):

    id = models.AutoField('id', primary_key=True)
    id_user = models.IntegerField('id заказчика')
    id_taxist = models.IntegerField('id таксиста')
    time = models.CharField('Время заказа', max_length=50)
    address1 = models.CharField('От куда', max_length=50)
    address2 = models.CharField('Куда', max_length=50)
    ordered_time = models.CharField('Заказанное время', max_length=50)
    tariff = models.CharField('Тариф', max_length=50)
    payment = models.CharField('Оплата', max_length=50)
    wishes = models.CharField('Пожелания', max_length=50)
    distance = models.IntegerField('Расстояние, км')
    cost = models.IntegerField('Стоимость, руб')

    def __str__(self):
        return self.id