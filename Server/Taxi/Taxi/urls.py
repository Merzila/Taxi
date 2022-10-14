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
from order.controller import order_response

from route.views import get_view_map, get_view_route
from autorization.views import autorization, registration
from order.views import create_order
from order.controller import order_response, cancel_of_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('route', get_view_route, name='get_view_route'),
    path('', get_view_map, name='get_view_map'),
    path('autorization', autorization, name = 'autorization'),
    path('registration', registration, name='registration'),
    path('order', create_order, name = 'create_order'),
    path('order/response', order_response, name = 'acceptance_of_order'),
    path('order/cancel', cancel_of_order, name = 'cancel of order')
    ]
