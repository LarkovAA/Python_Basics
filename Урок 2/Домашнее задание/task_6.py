print('Заполните информацию о товаре')
item_number = None
product = [] # создаю список всех продуктов
ex_t = None # создаю переменную для выхода из цикла
list_name, list_price, list_quantity, list_unit_measurement = [], [], [], []
# создал цикл в котором делаю запрос на добавления значений в словать и нумерацию. НА каждом цикле добавляю новый элемент нмера и словаря.
while True:
    # создаем словарь с характеристиками продукта
    product_characteristics = {}
    # создаем словарь для аналиа продуктов где значения это списки которые будут записываться при заполнении элементов словарей значениями
    product_analytics = {'название': list_name, 'цена': list_price, 'количество': list_quantity,
                         'ед-ца измерения': list_unit_measurement}
    # даю запрос на заполнения онформацией о товаре а так же жобавляю эти значения в соответствующие списки.
    item_number = input('Введите номер товара ? ')
    product_characteristics['название'] = input('Введите название товара ?  ')
    list_name.append(product_characteristics['название'])
    product_characteristics['цена'] = input('Введите цену товара ?  ')
    list_price.append(product_characteristics['цена'])
    product_characteristics['количество'] = input('Введите количество товара ?  ')
    list_quantity.append(product_characteristics['количество'])
    product_characteristics['ед-ца измерения'] = input('Введите единицу измерения товара ?  ')
    list_unit_measurement.append(product_characteristics['ед-ца измерения'])
    product.append((item_number, product_characteristics))

    # делаю запрос на выход из цикла
    ex_t = input('Вы ввели данные по товару. Хотите продолжить залолнение ?(Да или Нет) ')
    ex_t = ex_t.lower()
    if ex_t == 'нет':
        break

print(f'Вы ввели следующие данные {product}')
print(f'Выводим аналитическую информацию {product_analytics}')
