try:
    num_1 = int(input('Введите числитель '))
    num_2 = int(input('Введите знаминатель '))
except:
    print('Введите числа и цифры а не буквы')

def subdivision(num_1, num_2):
    try:
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        print('Делить на 0 нельзя')

answer = subdivision(num_1, num_2)
print(type(answer))
