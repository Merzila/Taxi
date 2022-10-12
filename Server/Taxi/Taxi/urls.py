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
from route.getroute import address_converter
from autorization.views import autorization, registration
from order.views import view
from order.expectation_of_taxist import expectation_of_taxist
from order.acceptance_of_order import acceptance_of_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', showroute, name='showroute'),
    path('', showmap, name='showmap'),
    path('autorization', autorization, name = 'autorization'),
    path('registration', registration, name='registration'),
    path('order', view, name = 'create_order'),
    path('order/expectation', expectation_of_taxist, name = 'expectation_of_taxist'),
    path('order/response', acceptance_of_order, name = 'acceptance_of_order')
    ]
