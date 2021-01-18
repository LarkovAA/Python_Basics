print('Заполните информацию о товаре')
item_number = None
product = [] # создаю список всех продуктов
ex_t = None # создаю переменную для выхода из цикла
# создал цикл в котором делаю запрос на добавления значений в словать и нумерацию. НА каждом цикле добавляю новый элемент нмера и словаря.
while True:
    product_characteristics = {}
    item_number = input('Введите номер товара ? ')
    product_characteristics['название'] = input('Введите название товара ?  ')
    product_characteristics['цена'] = input('Введите цену товара ?  ')
    product_characteristics['количество'] = input('Введите количество товара ?  ')
    product_characteristics['ед-ца измерения'] = input('Введите единицу измерения товара ?  ')

    product.append((item_number, product_characteristics))
    # делаю запрос на выход из цикла
    ex_t = input('Вы ввели данные по товару. Хотите продолжить залолнение ?(Да или Нет) ')
    ex_t = ex_t.lower()
    if ex_t == 'нет':
        break

print(f'Вы ввели следующие данные {product}')
# создал новый словарь где будет записаны значения всех ключей в созданых элементов словаря product
product_analytics = {'название': None, 'цена': None, 'количество': None, 'ед-ца измерения': None}
# создал списки в которых буду записывать все значения во всех созданых элементов по ключам
list_name, list_price, list_quantity, list_unit_measurement = [], [], [], []
# объеденил все созданные списки в один
list_product_characteristics = [list_name, list_price, list_quantity, list_unit_measurement]
# создал список всех ключей в списке product
list_prod_analy = ['название', 'цена', 'количество', 'ед-ца измерения']
# создал цикл который перебирает все элементы кортежа созданые в списке product
for el in product:
    num = 0
    for num_list in list_product_characteristics: # перебираем созданный вложеный список пустых списков
        num_list.append(el[1].get(list_prod_analy[num])) # добавляем в каждый пустой список значения какого то одного ключай
        num += 1
    # в новый словарь добавляем все значения который имеет каждый ключь во всех элементах соваря в списке product
    product_analytics['название'] = list_name
    product_analytics['цена'] = list_price
    product_analytics['количество'] = list_quantity
    product_analytics['ед-ца измерения'] = list_unit_measurement

print(f'Выводим аналитическую информацию {product_analytics}')