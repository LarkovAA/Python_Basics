'''
Вызывает в терминале имя каждой переменной и ее значение --name Aleksey
'''
from argparse import ArgumentParser

data_entry = ArgumentParser()

data_entry.add_argument('--name', type = str)
data_entry.add_argument('--production', type = int)
data_entry.add_argument('--bid', type = int)
data_entry.add_argument('--bonus', type = int, default= None)

calculation = data_entry.parse_args()
employee_compensation = {}

employee_compensation[calculation.name] = calculation.production * calculation.bid + calculation.bonus

print(f'У {list(employee_compensation.keys())[0]} заработная плата вышла в размере {employee_compensation[calculation.name]}')
