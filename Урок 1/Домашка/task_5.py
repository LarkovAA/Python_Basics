print('Добрый день вы в программе по определению экономической эффективности вашей организации')
revenue = int(input('Пожалуйста введите значение выручки '))
costs = int(input('Пожалуйста введите значение ваших издержек '))
result = revenue - costs # определяем есть ли прибыль у компании.

if result > 0:
    print(f'Поздравляем вы работаете в прибыль, она составляет {result}')
    print(f'Ваша рентабельность составила {result / revenue * 100} %')
    number_employees = int(input('Пожалуйств введите количество ваших сотрудников '))
    # определяем сколько принес в среднем прибыли  сотрудник
    profit_per_employee = result / number_employees
    print(f'В среднем один сик вам принес {profit_per_employee} прибыли')

elif result <=0:
    if result == 0:
        result = f'вы отработали в {result}'
    else:
        result = f'вы в убытке на {result}'
    print(f'Сожелею но вы не получаете прибыль ваш результат {result}')
