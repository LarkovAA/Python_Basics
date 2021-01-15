max = 0
number = int(input('Введите любое положительое число '))
while True:
    # определяем является ли число больше 1000 если да то идем по ветки if если нет то вычисляем сразу его максимальное число на ветке else
    if number >= 1000:
        # вычисляем число остатка
        num_min = number % 1000
        # приравниваем остаток целого числа в number
        number = number // 1000
        if num_min < 1000:
            # из вычисленного числа остатка высчитываем наибольшую цифру
            hundred_num = num_min // 100  # вычисляем сколько целых сотен есть в числе
            dozen_num = num_min % 100 / 10  # вычисляем сколько целых десятков есть в числе
            sungle_num = num_min % 10  # вычисляеть оставшуюся единицу числа
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
        hundred_num = number // 100  # вычисляем сколько целых сотен есть в числе
        dozen_num = number % 100 / 10  # вычисляем сколько целых десятков есть в числе
        sungle_num = number % 10  # вычисляеть оставшуюся единицу числа
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
print(f'Максимальная цифра вашего числа {int(max)}')


