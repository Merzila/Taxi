from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from .controller import checking_correctness, coding_psw
# Create your views here.

'''  В этом модуле описан Back-End для авторизации и регистрации пользователей '''

def registration(request, User=None, Phone=None, Name=None, Password=None, Password2 = None):

    '''  Регистрация пользователя '''

    Phone = checking_correctness(Phone, Name, Password)

    if len(Phone) == 11:

        if Name == None:
           return HttpResponse('Укажите своё имя!')
        elif Password == None:
           return HttpResponse('Придумайте пароль!')
        elif Password != Password2:
            return HttpResponse('Пароли не совпадают!')
        else:
            psw = coding_psw(Password)

            with sqlite3.connect('db.sqlite3') as db:
                sql = db.cursor()
                info = sql.execute(f" SELECT Phone FROM {User} WHERE Phone={Phone} ")
            
                if info.fetchone() is None:

                    if User == 'autorization_taxist':
                        sql.execute(f" INSERT INTO {User} (Phone, Name, Password, model_of_car, color_of_car, state_number) VALUES (?, ?, ?, ?, ?, ?) ", (Phone, Name, psw, 'None', 'None', 'None'))
                    else:
                        sql.execute(f" INSERT INTO {User} (Phone, Name, Password) VALUES (?, ?, ?) ", (Phone, Name, psw))

                    value = sql.execute(f" SELECT * FROM {User} WHERE Phone={Phone} ").fetchall()
                    db.commit()

                    return HttpResponse(f'OK,{value[0][0]},{value[0][1]},{value[0][2]}')

                else:
                    return HttpResponse('Пользователь с таким\n   номером телефона\n уже зарегистрирован!')

    else:
        return HttpResponse(f'{Phone}')

def autorization(requests, User=None, Phone=None, Password=None):

    '''  Авторизация и аутентификация пользователя '''
    Phone = checking_correctness(Phone, None, Password)

    if len(Phone) == 11:

        if Password == None:
            return HttpResponse('Введите пароль!')
        else:

            psw = coding_psw(Password)

            with sqlite3.connect('db.sqlite3') as db:
                
                sql = db.cursor()
            
                info1 = sql.execute(f" SELECT * FROM {User} WHERE Phone={Phone}")
                value = info1.fetchall()
                
                if value != []:
                    if value[0][3] == psw:
                        
                        return HttpResponse(f'OK,{value[0][0]},{value[0][1]},{value[0][2]}')
                    else:
                        return HttpResponse('Неверный пароль!')

                else:
                   return HttpResponse('Такого пользователя не существует!')

    else:
        return HttpResponse(f'{Phone}')