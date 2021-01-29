with open('file_task_5.txt', 'w', encoding='UTF-8') as file_task_5:
    number = True
    while number:
        number = input('Введите любые значения чисел (что бы завершить заполнение оставте пустую строчку) ')
        if bool(number) == True:
            try:
                number = int(number)
            except:
                print('Введите число а не буквы и слова')
            if type(number) == int:
                number = str(number)
                file_task_5.write(number + ' ')

with open('file_task_5.txt', 'r', encoding='UTF-8') as file_task_5:
    list_file_task_5 = file_task_5.read().split(' ')
    # Почемуто пустая строка добавляеться в список поэтому удаляем ее
    list_file_task_5.pop(len(list_file_task_5) - 1)
    summ_list_file_task_5 = sum(list(map(lambda x: int(x), list_file_task_5)))

    print(f'Сумма введенных вами чисел равен {summ_list_file_task_5}')
