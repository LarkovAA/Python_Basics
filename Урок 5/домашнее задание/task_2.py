with open('file_task_1.txt', 'r', encoding='UTF-8') as read_file:
    num_str = 0
    for el in read_file:
        num_char = len(el)
        num_str += 1
        print(f'Строка номер {num_str} имеет {num_char} символов')

