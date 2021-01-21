summ_num = 0
ext = None
while True:
    str_summ_num = input('Введите различные числа для определения их суммы (через пробел) для выхода наберите -q или -Q? ')
    list_summ_num = list(str_summ_num.split())
    if '-q' in list_summ_num or '-Q' in list_summ_num:
        ext = '-q'
        list_summ_num.remove(ext)
    list_summ_num = list(map(int, list_summ_num))
    summ_num = summ_num + sum(list_summ_num)
    print(f'Сумма введеных вами чисел равняеться {summ_num}')
    if ext == '-q':
        break

