# создаем список куда будем записывать элементы
list_data = []
# создаем цикл для записи элементов
while True:
    number = input('Введите введите элемент который хотите ввести ? (для выхода из вводп данных '
                   'наберите наберите :q или :Q ')
    if number == ':q' or number == ':Q':
        break
    list_data.append(number)
# создаем новый список куда будем записывать в обратном порядке соседние элементы
new_list_data = []
for el in range(1, len(list_data), 2):
    # перебираем все нечетные элементы ставим их на позицию el - 1
    new_list_data.insert(el - 1, list_data[el])
    new_list_data.insert(el, list_data[el - 1])

print(new_list_data)

