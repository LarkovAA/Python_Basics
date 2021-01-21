summ_num = 0
ext = None
# создаю цикл для сложения чисел
while True:
    str_summ_num = input('Введите различные числа для определения их суммы (через пробел) для выхода наберите -q или -Q? ')
    # создаем список со всеми значениями которые мы выше ввели
    list_summ_num = list(str_summ_num.split())
    # проверяем есть в данном списке значение -q
    if '-q' in list_summ_num or '-Q' in list_summ_num:
        ext = '-q'
        # удаляем это значение из списка
        list_summ_num.remove(ext)
    # переводим все элементы списка в числа
    list_summ_num = list(map(int, list_summ_num))
    summ_num = summ_num + sum(list_summ_num)
    print(f'Сумма введеных вами чисел равняеться {summ_num}')
    # в коде выше если слово имеется в списке введеных элементов то мы останавливаем цикл
    if ext == '-q':
        break

