class Division_0():
    def __str__(self):
        return f'Вы делите на 0. Так нельзя.'

num_1 = int(input('Ведите первое число ? '))
num_2 = int(input('Ведите второе число ? '))

try:
    rezult = num_1 / num_2
except:
    print(Division_0())
finally:
    if num_2 == 0:
        print(f'Ответ {num_1}')
    else:
        print(f'Ответ {rezult}')

