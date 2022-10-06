"""Taxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from audioop import add
from django.contrib import admin
from django.urls import path

from route.views import showroute, showmap
from route.getroute import address_converter, get_distance
from autorization.views import autorization, registration
from order.create_order import order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', showroute, name='showroute'),
    path('', showmap, name='showmap'),
    path('autorization/<str:User>,<str:Phone>,<str:Password>', autorization, name = 'autorization'),
    path('registration/<str:User>,<str:Phone>,<str:Name>,<str:Password>,<str:Password2>', registration, name='registration'),
    path('converter/<str:address1>,<str:address2>', address_converter, name = 'converter'),
    path('get_distance/<str:pickup_lat>,<str:pickup_lon>,<str:dropoff_lat>,<str:dropoff_lon>', get_distance, name='get_distance'),
    path('order/<str:id_user>,<str:time>,<str:ordered_time>,<str:tariff>,'+
        '<str:payment>,<str:wishes>', order, name = 'create_order')
    ]
