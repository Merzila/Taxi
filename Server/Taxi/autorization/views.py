from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from .controller import checking_correctness, hashing_password
from django.views.decorators.csrf import csrf_exempt
from .models import Users
# Create your views here.

'''  В этом модуле описан Back-End для авторизации и регистрации пользователей '''

@csrf_exempt
def registration(request):

    '''  Регистрация пользователя '''

    user = request.POST.get('user', '')
    phone = request.POST.get('phone', '')
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')

    phone = checking_correctness(phone, name, password)

    if len(phone) == 11:

        if name == None:
           return HttpResponse('Укажите своё имя!')
        elif password == None:
           return HttpResponse('Придумайте пароль!')
        else:

            password = hashing_password(password)

            try:
                eval(f'{user}').objects.get(phone = phone)

                return HttpResponse('Пользователь с таким номером телефона уже зарегистрирован!')

            except:

                u = eval(f'{user}').objects.create(phone = phone, name = name, password = password)

                return HttpResponse(f'OK,{u.pk}')

    else:
        return HttpResponse(f'{phone}')

@csrf_exempt
def autorization(request):

    '''  Авторизация и аутентификация пользователя '''

    user = request.POST.get('user', '')
    phone = request.POST.get('phone', '')
    password = request.POST.get('password', '')

    phone = checking_correctness(phone, None, password)

    if len(phone) == 11:

        if password == None:
            return HttpResponse('Введите пароль!')
        else:

            password = hashing_password(password)

            try:
                u = eval(f'{user}').objects.get(phone = phone)
                
                print(u.password, type(u.password))
                print(password, type(u.password))

                if u.password == password:
                    return HttpResponse(f'OK,{u.pk}')
                else:
                    return HttpResponse('Неверный пароль!')

            except:
                return HttpResponse('Такого пользователя не существует!')

    else:
        return HttpResponse(f'{phone}')