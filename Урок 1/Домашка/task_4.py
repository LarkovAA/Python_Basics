max = None
while True:
    number = int(input('Введите любое положительое число больше 10 но меньше 1000? '))
    if number >= 10 and number < 1000:
        hundred_num = number // 100 # вычисляем сколько целых сотен есть в числе
        dozen_num = number % 100 / 10  # вычисляем сколько целых десятков есть в числе
        number = number % 10 # вычисляеть оставшуюся единицу числа
        # делаем проверку какое число единичное или десятка больше и записывем в переменную max
        if number >= dozen_num:
            max = number
        else:
            max = dozen_num
        if max >= hundred_num:
            max = max
        else:
            max = hundred_num
        print(f'Самая большая цифра из вашего числа {max}')
        break
