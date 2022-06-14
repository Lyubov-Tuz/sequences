num_sequence = input('Введите элементы списка через запятую: ').replace(';', ',').replace('/', ',').split(',')
numbers_list = list(set(num_sequence))
print(numbers_list)