import hashlib

def checking_correctness(phone, name, password):

    '''  Проверка корректности введённых пользователем данных '''

    with open('autorization/alphabet for authorization.txt', encoding = 'utf-8') as alp:
        list_for_phone = alp.readline().split()[1]
        list_for_name = alp.readline().split()[1]
        list_for_password = alp.readline().split()[1]
        
    if phone[:2] == '+7':
        phone = phone.replace('+7', '8', 1)

    if len(phone) != 11 or phone[0] != '8':
        return 'Неправильный формат\n     номера телефона!'

    for i in phone:
        if not (i in list_for_phone):
            return 'Неправильный формат\n     номера телефона!'

    if name is not None:
        for i in name:
            if not (i in list_for_name):
                return 'Неправильный формат\n             имени!'

    for i in password:
        if not (i in list_for_password):
            return 'Неправильный формат\n             пароля!'
    
    return phone

def hashing_password(password):

    return hashlib.md5(eval("b'"+f"{password}"+"'")).digest()