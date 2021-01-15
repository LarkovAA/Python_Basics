max = 0
number = int(input('Введите любое положительое число '))
while True:
    if number >= 1000:
        number = number // 1000
        num_min = number % 1000
        if num_min < 1000:
            hundred_num = int(num_min // 100)  # вычисляем сколько целых сотен есть в числе
            dozen_num = int(num_min % 100 / 10)  # вычисляем сколько целых десятков есть в числе
            sungle_num = int(num_min % 10)  # вычисляеть оставшуюся единицу числа
        # делаем проверку какое число единичное или десятка больше и записывем в переменную max
            if max >= sungle_num:
                max = max
            else:
                max = sungle_num
            if max >= dozen_num:
                max = max
            else:
                max = dozen_num
            if max >= hundred_num:
                max = max
            else:
                max = hundred_num

    else:
        hundred_num = int(number // 100)  # вычисляем сколько целых сотен есть в числе
        dozen_num = int(number % 100 / 10)  # вычисляем сколько целых десятков есть в числе
        sungle_num = int(number % 10)  # вычисляеть оставшуюся единицу числа
        # делаем проверку какое число единичное или десятка больше и записывем в переменную max
        if max >= sungle_num:
            max = max
        else:
            max = sungle_num
        if max >= dozen_num:
            max = max
        else:
            max = dozen_num
        if max >= hundred_num:
            max = max
        else:
            max = hundred_num
        break
print(f'Максимальная цифра вашего числа {max}')


