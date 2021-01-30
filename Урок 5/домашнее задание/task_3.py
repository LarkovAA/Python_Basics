# создаем список где будем хранить в виде словаря данные
list_empl_data = []
sur_name = True
salary = True
# открываем файл на запись
with open('file_task_3.txt', 'w', encoding='UTF-8') as fil_tas_3:
    # создем словарь в котором будем записывать фамилию и оклад сотрудника
    employee_data = {}
    # в цикле запрашиваем ввод данных
    while sur_name:
        sur_name = input('Введите фамилию сотрудника (для выхода оставте пустую строчку) ')
        # проверяеи на наличии ошибки
        try:
            salary = int(input('Введите оклад сотрудника (для выхода поставте 0) '))
            # если ввели отрицательное число то мы генерируем ошибку неправильного значения
            if salary < 0:
                raise ValueError
        except ValueError:
            print('Введите положительное число а не буквы !!')
        # проверяем если запрос на ввод фамилии дае правду и значение переменной оклада больше 0
        if bool(sur_name) == True and salary > 0:
            # записываем новые значения в словарь
            employee_data[sur_name] = salary
            # новый словарь записываем в файл
            fil_tas_3.write(f'{employee_data} \n')
            # записываем словарь в список
            list_empl_data.append(employee_data.copy())
            # очишаем словарь от значений
            employee_data.clear()

# создаем новый список в котором храним данные сотрудников имеющих оклад больше 20000
new_list_20000 = [el for el in list_empl_data if int(list(el.values())[0]) > 20000]
# создаем список фамилий сотрудников имеющих оклад больше 20000
surname_list = list(map(lambda x: list(x.keys())[0], new_list_20000))
# создаем список содержащий все значения окладов работников
list_average_salary = list(map(lambda x: list(x.values())[0], list_empl_data))
# создаем переменную в которой высчитываем значение средней заработной платы
average_salaty = sum(list_average_salary) / len(list_average_salary)

print(f'Данные сотрудники имеют оклад больше 20000: {surname_list}')
print(f'Среднее значение окладов работников составляет: {average_salaty}')
