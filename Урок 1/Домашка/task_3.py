number = input('Введите число от 1 до 9 для того что бы найти сумму чисел n + nn + nnn ? ')
# используя конкатенацию объеденяем полученное число для создания десятичной ормы
dozen_num = number + number
# аналогично делаем то же самое для создании сотен
hundred_num = dozen_num + number
print(f'сумма вашего числа равняется {int(number) + int(dozen_num) + int(hundred_num)}')
