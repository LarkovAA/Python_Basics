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
for el in range(0, len(list_data)):
    # вводим новую переменную для определения четности номера элемента
    num_el = el % 2
    # если номер элемента четный то мы добавляем его на туже позицию
    if num_el == 0:
        new_list_data.append(list_data[el])
    # если нечетный то ставим его на позицию el - 1
    if num_el == 1:
        new_list_data.insert(el - 1, list_data[el])

print(new_list_data)

