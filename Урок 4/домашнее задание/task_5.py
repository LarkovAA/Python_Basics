from functools import reduce
list_num = [num for num in range(100, 1001) if num % 2 == 0]

def summ_num(num_1, num_2):
    return num_1 + num_2

print(f'Сумма всех четных элементов списка {reduce(summ_num, list_num)}')

