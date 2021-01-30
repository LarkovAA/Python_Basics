with open('file_task_5.txt', 'w', encoding='UTF-8') as file_task_5:
    number = True
    # в цикле производим ввод данных пока переменная имеет значение True
    while number:
        number = input('Введите любые значения чисел (что бы завершить заполнение оставте пустую строчку) ')
        # если переменная имеет значение тру то мы производим изменение типа данных на число если изиенить тип данных не полуается то выводим ошибку
        if bool(number) == True:
            try:
                number = int(number)
            except:
                print('Введите число а не буквы и слова')
            # если в итоге переменная является число то мы снова переводим в строку и записываем в файл
            if type(number) == int:
                number = str(number)
                file_task_5.write(number + ' ')

with open('file_task_5.txt', 'r', encoding='UTF-8') as file_task_5:
    # создаем список в который записываем все элементы в файле с помоью разделителя пробела
    list_file_task_5 = file_task_5.read().split(' ')
    # Почемуто пустая строка добавляеться в список поэтому удаляем ее
    list_file_task_5.pop(len(list_file_task_5) - 1)
    # переводим все элементы списка в тип число и суммируем их
    summ_list_file_task_5 = sum(list(map(lambda x: int(x), list_file_task_5)))

    print(f'Сумма введенных вами чисел равен {summ_list_file_task_5}')
