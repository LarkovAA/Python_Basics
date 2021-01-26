from functools import reduce
# создаем список с помошью генератора всех четных чисе от 100 до 1000
list_num = [num for num in range(100, 1001) if num % 2 == 0]
# создаем функцию в которой каждый элемент с помошью функции reduce будем суммировать
def summ_num(num_1, num_2):
    return num_1 + num_2

print(f'Сумма всех четных элементов списка {reduce(summ_num, list_num)}')

