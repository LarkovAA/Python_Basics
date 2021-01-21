def subdivision(num_1, num_2):
    try:
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        print('Делить на 0 нельзя')

num_1 = ''
num_2 = ''

while type(num_1) == str and type(num_1) == str:
    try:
        num_1 = int(input('Введите числитель '))
        num_2 = int(input('Введите знаминатель '))
    except:
        print('Введите числа и цифры а не буквы')

subdivision(num_1, num_2)