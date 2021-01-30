with open('file_task_6.txt', 'r', encoding='UTF-8') as file_t_6:
    readlines_file_t_6 = file_t_6.readlines()
    list_file_t_6 = []

    for file_str in readlines_file_t_6:
        list_file_t_6.append(file_str.split(','))
    key_dict = []
    value_dict = []

    for list_el in list_file_t_6:
        for str_el in list_el:
            key_dict.append(str_el[: str_el.index(':')])
            value_dict.append(str_el[str_el.index(':') + 1:])
    value_dict = list(map(lambda x: x.split(' '), value_dict))

    new_value_dict = []
    for el in value_dict:
        try:
            new_value_dict.append(copy_num_el)
        except:
            pass
        copy_num_el = []
        for num_el in el:
            if num_el == '' or num_el == '-\n':
                continue
            else:
                number = ''
                for int_el in num_el:
                    try:
                        if type(int(int_el)) == int:
                            number = number + int_el
                    except:
                        continue
                copy_num_el.append(number)

    new_value_dict = list(map(lambda x: list(map(lambda y: int(y), x)), new_value_dict))

    dara_items = {}
    for num in range(0, len(key_dict) - 1):
        dara_items[key_dict[num]] = sum(new_value_dict[num])

    print(f'По итогу каждый предмет имеет следующее колличество часов на обучение {dara_items}')








'''
                       for int_el in num_el:
                try:
                    if type(int(int_el)) == int:
                        num = num + int_el
                        value_dict[value_dict.index(el)][el.index(num_el)] = num
                except:
                    continue
    print(value_dict)
           '''

'''
    list_value_dict = list(map(lambda x: x.split(' '), value_dict))
    print(list_value_dict)

    copy_list_value_dict =  list_value_dict.copy()

    for el in list_value_dict:
        #print(f'1 уровень {el}')
        list_el = []

        for str_el in el:
            list_str_el = []
            #print(f'2 уровень {str_el}')
            for int_el in str_el:
                if int_el == '(':
                    list_str_el = []
                #print(f'3 уровень {int_el}')
                try:
                    if type(int(int_el)) == int:
                        number = int_el
                        list_str_el.append(number)
                        list_el.append(list_str_el)
                        list_str_el = []
                        list_value_dict[list_value_dict.index(el)] = list_el
                except:
                    continue

   '''