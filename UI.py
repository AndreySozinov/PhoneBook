def entry():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comments = input('Введите описание: ')
    data = [last_name, first_name, phone, comments]
    return data

def deleting():
    index = int(input('Введите номер записи которую нужно удалить (начиная с 0): '))
    return index

def symbol():
    input('Введите "y" если разделитель ; ')
    if input.lower == "y":
        sign = ";"
    else: sign = "\n"
    return sign