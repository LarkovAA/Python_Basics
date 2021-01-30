import json
# открываем файл на чтение
with open('file_task_7.txt', 'r', encoding='UTF-8') as file_t_7:
    file_t_7 = file_t_7.readlines()
    # создаем список в который запишем списки составленные из элементов файла разделенные через пробел
    list_file_t_7 = []
    for el in file_t_7:
        el = list(el.split())
        list_file_t_7.append(el)
    # создаем словарь из значений списка list_file_t_7
    data_company = {}
    for el in range(0, len(list_file_t_7)):
        data_company[f'{list_file_t_7[el][1]} {list_file_t_7[el][0]}'] = int(list_file_t_7[el][2]) - int(list_file_t_7[el][3])
    # в данную переменную записываем значение средней прибыли компании
    average_profit = sum(list(data_company.values())) / len(data_company)
    # создаем переменную в которую записываем полученные данные из словаря и переменной средней значений прибыли
    general_company_data = f'общие данные по компаниям составляют {data_company} срдняя прибыль компаний составляет {average_profit}'
    # добавляем полученные данные в файл формата json
with open('file_task_7.json', 'w', encoding='UTF-8') as file_t_7_json:
    json.dump(general_company_data, file_t_7_json)