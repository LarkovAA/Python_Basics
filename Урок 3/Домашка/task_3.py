num_1 = int(input('Введите ваше первое число? '))
num_2 = int(input('Введите ваше второе число? '))
num_3 = int(input('Введите ваше третье число? '))

def my_func(num_1, num_2, num_3):
    list_max = [num_1, num_2, num_3]
    max_1 = max(list_max)
    list_max.remove(max_1)
    max_2 = max(list_max)
    print(f'Сумма двух максимальных чисел равняеться {max_1 + max_2}')

my_func(num_1, num_2, num_3)