import time
from itertools import count, cycle
from random import randint
# запрашиваем данные
number = int(input('С какого числа начать генерацию чисел '))
max_number = int(input('Сколько элементов генерировать ? '))
# с помошью цикла выводим значения начиная с выбранного числа и останавливаемся когда достигнем того количества эллементов которые мы выбрали
for num in count(number):
    if num > number + max_number - 1:
        break
    else:
        print(num)
        time.sleep(1)

# создаем список
list_name = []
el_num = int(input('Какое колличество элементов генерироватьв списке ? '))
# в этот список записываем случайные элементы
for num in range(1, el_num + 1):
    gener_num = randint(0, 1000)
    list_name.append(gener_num)

print(f'{list_name} получившийся списко')

iterm = cycle(list_name)
# выводим каждое значение списка 3 раза
for num in range(1, len(list_name * 3) + 1):
    print(next(iterm))
    time.sleep(1)
