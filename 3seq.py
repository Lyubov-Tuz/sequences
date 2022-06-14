num_sequence_1 = input('Введите элементы первого списка через запятую: ').replace(';', ',').replace('/', ',').split(',')

num_sequence_2 = input('Введите элементы второго списка через запятую: ').replace(';', ',').replace('/', ',').split(',')

for i in num_sequence_1[::-1]:
    if i in num_sequence_2:
         num_sequence_1.remove(i)

print(f'Результат: {num_sequence_1}')
