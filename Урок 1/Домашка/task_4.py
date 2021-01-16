max = 0
stop_cicle = False
number = int(input('Введите любое положительое число '))
# если введенное чисо меньше десяти то мы прибавляем к этому значению 10
if number >= 1 and number <= 9:
    number = number + 10
while number // 10 !=0:
    # находим остаток от введенного числа
    number_min = number % 10
    # от определенного остатка находим являеться ли оно больше переменной max
    if number_min >= max:
        max = number_min
    else:
        max = max
    number = number // 10
    if number >= 1 and number <= 9:
        number = number + 10
        stop_cicle = True
    if stop_cicle == True:
        break
print(f'Самая большая цифра в вашем числе это {max}')
