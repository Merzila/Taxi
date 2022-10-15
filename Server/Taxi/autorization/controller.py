import hashlib

def checking_correctness(phone, name, password):

    # Проверка корректности введённых пользователем данных

    with open('autorization/alphabet for authorization.txt', encoding = 'utf-8') as alp:
        list_for_phone = alp.readline().split()[1]
        list_for_name = alp.readline().split()[1]
        list_for_password = alp.readline().split()[1]

    if phone == None:
        return 'Введите номер телефона!'
    if name == None:
        return 'Укажите своё имя!'
    if password == None:
        return 'Придумайте пароль!'

    if len(phone) != 10:
        return 'Неправильный формат номера телефона!'

    for i in phone:
        if not (i in list_for_phone):
            return 'Неправильный формат номера телефона!'

    if name is not None:
        for i in name:
            if not (i in list_for_name):
                return 'Неправильный формат имени!'

    for i in password:
        if not (i in list_for_password):
            return 'Неправильный формат пароля!'
    
    return phone

def hashing_password(password):

    # Хеширование пароля

    return hashlib.md5(eval("b'"+f"{password}"+"'")).digest()