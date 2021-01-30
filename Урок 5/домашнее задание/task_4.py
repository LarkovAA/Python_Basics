# создаем список переведенных слов
translation = ['Один', 'Два', 'Три', 'Четыре']
# создаем пустой список в котором запишем данные каждой строки
new_list_file_t_4 = []
with open('file_task_4.txt', 'r', encoding='UTF-8') as file_t_4:
    num = 0
    for str_line in file_t_4:
        # записываем в список значение каждой из строк
        list_str = str_line.split(' ')
        # меняем первое значение списка на значение их списка с переводом
        list_str[0] = translation[num]
        num += 1
        # каждый список переведенный из строки записываем в новый список
        new_list_file_t_4.append(list_str)

# создаем переменную в которой запишем переведенные данные
new_str_file_t_4 = ''
for el in new_list_file_t_4:
    new_str_file_t_4 = new_str_file_t_4 + ' '.join(el)
# открываем файл и записываем в него значения переменной которую создали выше
with open('new_file_task_4.txt', 'w', encoding='UTF-8') as new_file_t_4:
    new_file_t_4.write(new_str_file_t_4)