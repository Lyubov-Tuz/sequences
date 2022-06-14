# списки list
furniture = ['стол', 'стул', 'кровать', 'диван', 'кресло', 'шкаф']
print(type(furniture))
print(furniture)

furniture.append('трюмо') #добавить элемент
print(furniture)

furniture.remove('стул') #удаляет

furniture.sort() #сортировка
print(furniture)

furniture.insert(2, 'стульчик') # вставляет i элемент на значение х
print(furniture)

furniture.pop() #удаляет элемент. Если элемент не указан, то удаляется последний элемент
print(furniture)

# словари dict
friends = {
    'name': 'leo',
    'age': 25,
    'has_car': True
}
print(type(friends))
print(friends)

print(len(friends)) #длина
print('name' in friends) # Проверяет по ключам
print(friends) # Добавить, Изменить
friends['has_wife'] = False
print(friends)
friends['has_wife'] = True
print(friends)
del friends['has_wife'] #удалить
print(friends)

print('max' in friends.values())


# множества set
food = {'овощи', 'фрукты', 'напитки', 'сладкое'}
print(type(food))
print(food)

menu = {'овощи', 'острое', 'напитки', 'выпечка'}
print(type(menu))
print(menu)

print(food.isdisjoint(menu)) # проверка, что не имеют общих элементов
print((food in menu))# принадлежит ли множество другому множеству
print(food.add('закуска')) #добавляет элемент
print(food.difference(menu))# элементы одного множества не принадлежат другому
print((food.union(menu))) # объединение


# строки str

muza = 'Мороз и солнце - день чудесный'
print(type(muza))
print(muza)

print(muza.upper()) # преобразование к верхнему регистру
print(muza.title()) # первая буква - верхний регистр, остальные в нижний
print(muza.lower()) # преобразование к нижнему регистру
print(muza.isdigit()) # состоит ли строка из цифр
print(muza.split('-')) # разбиение строки поразделителю