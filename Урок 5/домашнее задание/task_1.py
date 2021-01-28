with open('file_task_1.txt', 'w', encoding='UTF-8') as file_t_1:
    data_str = True
    while data_str:
        data_str = input('Введите строку которую хотите добавить. ')
        file_t_1.write(data_str + '\n')

with open('file_task_1.txt', 'r', encoding='UTF-8') as file_t_1:
    data_read_file = file_t_1.read()
    print(data_read_file)
