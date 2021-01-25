from itertools import count, cycle
from random import randint
number = int(input('С какого числа начать генерацию чисел '))
max_number = int(input('Сколько элементов генерировать ? '))

for num in count(number):
    if num > number + max_number - 1:
        break
    else:
        print(num)

list_name = []

for num in range(1, 15):
    gener_num = randint(0, 1000)
    list_name.append(gener_num)

iterm = cycle(list_name)

for num in range(1, len(list_name * 3)):
    print(next(iterm))

