print('------ You are welcome ------')
import pickle
dict1 = {}
while True:
    x = input('«Пожалуйста, введите действие, которое вы хотите сделать: если вы новичок или изменены на« 1 », запрос:« 2 », удалить« 3 »: ')
    # Словарь сериализации данных хранения
    with open('addressbook.txt', 'ab+') as io1:
        pickle.dump(dict1, io1)
    #    .
    i = 0
    while i < 50 : #   50 раз
        i += 1
        with open('addressbook.txt', 'rb+') as io2:
            res= dict(pickle.load(io2))
            dict1.update(res)
    if x == '1':
        name = input('Пожалуйста, введите Ваше имя:')
        tel = input('Пожалуйста введите ваш номер телефона')
        dict1[name] = tel
        print('«Успешно»')
    elif x == '2':
        print(dict1)
        name2 = input('«Пожалуйста, введите имя, которое Вам нужно найти»')
        print('% s Телефон:% s' %(name2,dict1.get(name2)))
    elif x == '3':
        name3 = input('«Пожалуйста, введите контакт для удаления»')
        if name3 in dict1.keys():
            del dict1[name3]
            print('«Контакт% s Удалить успех» %(name3)')
        else:
            print('«такого контакта не существует»')