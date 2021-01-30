with open('file_task_6.txt', 'r', encoding='UTF-8') as file_t_6:
    # открываем файл на чтение и записываем в список данные этого файла
    readlines_file_t_6 = file_t_6.readlines()
    list_file_t_6 = []

    # проходим по каждому элементу нового списка и делин его по запятой
    for file_str in readlines_file_t_6:
        list_file_t_6.append(file_str.split(','))
    # создаем два списка в которых будем содержать элементы ключей и значений
    key_dict = []
    value_dict = []
    # дабавляем путем деление строк на : до знака : все элементы мы передаем в ключи а после в значения
    for list_el in list_file_t_6:
        for str_el in list_el:
            key_dict.append(str_el[: str_el.index(':')])
            value_dict.append(str_el[str_el.index(':') + 1:])
    # сам спикок со значениями мы разбиваем по пробелу
    value_dict = list(map(lambda x: x.split(' '), value_dict))

    # создаем новый список со значениями в который мы запишем строки которые могут перевестись в тип данных число
    new_value_dict = []
    for el in value_dict:
        # записываем в новый словарь значений список который будет содержать элементы которые могут изменить значение на число
        # если взникает ошибка то мы ее пропускаем
        try:
            new_value_dict.append(copy_num_el)
        except:
            pass
        # создан словарь который и будет содержать строки которые могут перевестись в числа
        copy_num_el = []
        for num_el in el:
            # если элемент содержит пустую строку или просто - или со знком преноса то мы пропускаем данный элемент
            if num_el == '' or num_el == '-\n' or num_el == '-':
                continue
            else:
                # создаем переменную в которой будем из каждого элемента записывать строки имеющие тип значния числа
                number = ''
                for int_el in num_el:
                    try:
                        if type(int(int_el)) == int:
                            number = number + int_el
                    except:
                        continue
                # записываем данную переменную в список
                copy_num_el.append(number)
                # если мы рассматриваем послежний элемент в списке value_dict то записываем данные сразуже после заполнения списка copy)num_el
                if len(value_dict) - 1 == value_dict.index(el):
                    new_value_dict.append(copy_num_el)
    # все элементы нового списка значений мы меняем тип на числа
    new_value_dict = list(map(lambda x: list(map(lambda y: int(y), x)), new_value_dict))
    # создаем словарь и записываем в него новые элементы
    print(len(key_dict))
    dara_items = {}
    for num in range(0, len(key_dict)):
        dara_items[key_dict[num]] = sum(new_value_dict[num])

    print(f'По итогу каждый предмет имеет следующее колличество часов на обучение {dara_items}')