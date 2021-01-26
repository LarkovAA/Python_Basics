from random import randint
# деаем запрос на колличество элеменнтов в соваре
max_list_len = int(input('Какое колличество элементов будет в словаре ? '))
# создаем словарь
list_num = []
# заполняем словарь
while len(list_num) <= max_list_len:
    random_num = randint(0, 1000)
    list_num.append(random_num)
print(f'был сформирован следующий список {list_num}')
# создаем новый список с помошью генерации в который будут записываться значения: если элемент больше предыдушего то его мы записываем
new_list_num = [num for num in list_num[1:] if num >= list_num[list_num.index(num) - 1]]

print(f'Новый сформированный список {new_list_num}')
