print('Заполните информацию о товаре')
item_number = None
product = []
ex_t = None

while True:
    product_characteristics = {}
    item_number = input('Введите номер товара ? ')
    product_characteristics['название'] = input('Введите название товара ?  ')
    product_characteristics['цена'] = input('Введите цену товара ?  ')
    product_characteristics['количество'] = input('Введите количество товара ?  ')
    product_characteristics['ед-ца измерения'] = input('Введите единицу измерения товара ?  ')

    product.append((item_number, product_characteristics.copy()))

    ex_t = input('Вы ввели данные по товару. Хотите продолжить залолнение ?(Да или Нет) ')
    ex_t = ex_t.lower()
    if ex_t == 'нет':
        break

print(f'Вы ввели следующие данные {product}')

product_analytics = {'название': None, 'цена': None, 'количество': None, 'ед-ца измерения': None}
list_name, list_price, list_quantity, list_unit_measurement = [], [], [], []
list_product_characteristics = [list_name, list_price, list_quantity, list_unit_measurement]
list_prod_analy = ['название', 'цена', 'количество', 'ед-ца измерения']

for el in product:
    num = 0
    for num_list in list_product_characteristics:
        num_list.append(el[1].get(list_prod_analy[num]))
        num += 1
    product_analytics['название'] = list_name
    product_analytics['цена'] = list_price
    product_analytics['количество'] = list_quantity
    product_analytics['ед-ца измерения'] = list_unit_measurement

print(f'Выводим аналитическую информацию {product_analytics}')