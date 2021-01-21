characteristic_values = [{'название': ['компьютер', 'принтер', 'сканер']}, {'цена': [20000, 6000, 2000]}, {'количество': [5, 2, 7]},
                         {'ед': ['шт']}]

print(characteristic_values[1].values())
characteristic_values[1]['цена'] = list(map(lambda x: list(map(lambda y: y * 90, x)), characteristic_values[1].values()))

print(characteristic_values)