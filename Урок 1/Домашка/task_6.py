print('Добрый день вы находитесь в программе калькулятора тренировок.')
result_1_day = int(input('Введите сколько километров вы пробежали за 1 день ? '))
result = int(input('Какого значения вы хотите достигнуть ? '))

day = 1
while result_1_day <= result:
    result_1_day = result_1_day * 1.1
    day += 1

print(f'Вы достигните своей цели за {day} дня')