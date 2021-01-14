number = 1993
print(f'Выведено число : {number}')
name = 'Алексей'
print(f'Выведено сово : {name}')
rate_dol = 73.80
print(f'Выведен курс доллара : {rate_dol}')

year = input('Введите год вашего рождения ? ')
print(f'Вы ввели {year} год рождения')
name = input('Введите ваше имя ? ')
print(f'Вы ввели имя {name}')
last_name = input('Введите вашу фамилию ? ')
print(f'Вы ввели фамилию {last_name}')
children = input('У вас есть дети ? (Да/Нет) ')
children = children.lower()
if children == 'да':
    number_children = input('Сколько у вас детей ? ')
    text_depending_on_children = f'у вас {number_children} детей'
else:
    text_depending_on_children = f'у вас нет детей'
print(f'Вас зовут {name} {last_name}, вы {year} года рождения и {text_depending_on_children} ')
