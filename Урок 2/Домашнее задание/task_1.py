list_elem = ['int', 1993, True, 3.14, [1, 2, 3], (4, 5, 6), {1, 2, 3, 2},
                 {'key_1': 'val_1', 'key_2': 'val_2'}, b'bytes', 3 + 14j]

for el in list_elem:
    tyoe_el = type(el)
    print(f'У элемента {el} тип {tyoe_el}')
