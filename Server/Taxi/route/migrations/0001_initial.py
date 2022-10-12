# Generated by Django 4.1.2 on 2022-10-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.TextField(verbose_name='Маршрут')),
                ('coordinate_start', models.CharField(max_length=100, verbose_name='Начальные координаты')),
                ('coordinate_end', models.CharField(max_length=100, verbose_name='Конечные координаты')),
                ('address_start', models.CharField(max_length=100, verbose_name='Начальный адрес')),
                ('address_end', models.CharField(max_length=100, verbose_name='Конечный адрес')),
                ('distance', models.FloatField(verbose_name='Дистанция, км')),
                ('map', models.TextField(verbose_name='Карта, html')),
            ],
        ),
    ]
