try:
    number_entered = int(input('Введите число факториал которого хотите расчитать '))
except:
    print('Введите число')

def fact(num):
    if num == 1:
        yield 1
    yield next(fact(num - 1)) * num

for el in fact(number_entered):
    print(f'факториал числа {number_entered} равняется {el}')