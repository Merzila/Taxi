from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from .controller import checking_correctness, hashing_password
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

'''  В этом модуле описан Back-End для авторизации и регистрации пользователей '''

@csrf_exempt
def registration(request):

    '''  Регистрация пользователя '''

    User = 'autorization_' + request.POST.get('user', '')
    Phone = request.POST.get('phone', '')
    Name = request.POST.get('name', '')
    Password = request.POST.get('password', '')

    Phone = checking_correctness(Phone, Name, Password)

    if len(Phone) == 11:

        if Name == None:
           return HttpResponse('Укажите своё имя!')
        elif Password == None:
           return HttpResponse('Придумайте пароль!')
        else:

            Password = hashing_password(Password)

            with sqlite3.connect('db.sqlite3') as db:
                sql = db.cursor()
                info = sql.execute(f" SELECT Phone FROM {User} WHERE Phone={Phone} ")
            
                if info.fetchone() is None:

                    if User == 'autorization_taxist':
                        sql.execute(f" INSERT INTO {User} (Phone, Name, Password, model_of_car, color_of_car, state_number) VALUES (?, ?, ?, ?, ?, ?) ", (Phone, Name, Password, 'None', 'None', 'None'))
                    else:
                        sql.execute(f" INSERT INTO {User} (Phone, Name, Password) VALUES (?, ?, ?) ", (Phone, Name, Password))

                    value = sql.execute(f" SELECT id FROM {User} WHERE Phone={Phone} ").fetchall()
                    db.commit()

                    return HttpResponse(f'OK,{value[0][0]}')

                else:
                    return HttpResponse('Пользователь с таким номером телефона уже зарегистрирован!')

    else:
        return HttpResponse(f'{Phone}')

@csrf_exempt
def autorization(request):

    '''  Авторизация и аутентификация пользователя '''

    User = 'autorization_' + request.POST.get('user', '')
    Phone = request.POST.get('phone', '')
    Password = request.POST.get('password', '')

    Phone = checking_correctness(Phone, None, Password)

    if len(Phone) == 11:

        if Password == None:
            return HttpResponse('Введите пароль!')
        else:

            Password = hashing_password(Password)

            with sqlite3.connect('db.sqlite3') as db:
                
                sql = db.cursor()
            
                info1 = sql.execute(f" SELECT * FROM {User} WHERE Phone={Phone}")
                value = info1.fetchall()
                
                if value != []:
                    if value[0][3] == Password:
                        
                        return HttpResponse(f'OK,{value[0][0]}')
                    else:
                        return HttpResponse('Неверный пароль!')

                else:
                   return HttpResponse('Такого пользователя не существует!')

    else:
        return HttpResponse(f'{Phone}')