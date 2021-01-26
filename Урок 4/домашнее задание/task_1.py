'''
Вызывает в терминале имя каждой переменной и ее значение --name Aleksey
'''
# импортируем библиотеку и функцию
from argparse import ArgumentParser

data_entry = ArgumentParser()

# задаем переменные дя значений
data_entry.add_argument('--name', type = str)
data_entry.add_argument('--production', type = int)
data_entry.add_argument('--bid', type = int)
data_entry.add_argument('--bonus', type = int, default= None)

# в пемеменную calculation получаем значения всех переменных
calculation = data_entry.parse_args()
# создаем словарь куда записываем занчения
employee_compensation = {}
# расчитываем по заданным данным
employee_compensation[calculation.name] = calculation.production * calculation.bid + calculation.bonus
# выводим на экран информацию какому сотруднику была начислена какая заработная пата
print(f'У {list(employee_compensation.keys())[0]} заработная плата вышла в размере {employee_compensation[calculation.name]}')
