
list_data = []

while True:
    number = input('Введите введите элемент который хотите ввести ? (для выхода из вводп данных '
                   'наберите наберите :q или :Q ')
    if number == ':q' or number == ':Q':
        break
    list_data.append(number)

new_list_data = []
for el in range(0, len(list_data)):
    num_el = el % 2
    if num_el == 0:
        new_list_data.append(list_data[el])
    if num_el == 1:
        new_list_data.insert(el - 1, list_data[el])

print(new_list_data)

