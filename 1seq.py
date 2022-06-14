number = input('Введите кол-во элементов: ')
while not number.isdigit():
    number = input('Введите кол-во элементов целым числом: ')
size = []
for i in range(1, int(number) + 1):
    element = input(f'Введите {i}-й элемент: ')

    while not element.isdigit():
        element = input(f'Введите {i}-й элемент целым числом: ')

    size.append(int(element))
size.sort()

print(f'\nВывод: {size}')
