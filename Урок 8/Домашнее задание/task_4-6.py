class Office_equipment_warehouse():
    warehouse = []
    division = []

    @staticmethod
    def admission_warehouse(office_equipment, quantity):
        try:
            Office_equipment_warehouse.chekink_int(quantity)
        except:
            return print('Колличество техники вы ввели не числом а строкой')
        else:
            dic_admis_wareh = {}
            dic_admis_wareh[office_equipment] = quantity
            Office_equipment_warehouse.warehouse.append(dic_admis_wareh)

    @staticmethod
    def transfer_divisions(company_division, quantity, office_equipment):
        try:
            Office_equipment_warehouse.chekink_int(quantity)
        except:
            return print('Колличество техники вы ввели не числом а строкой')
        else:
            for el in Office_equipment_warehouse.warehouse:
                keys_wareh = tuple(el.keys())[0]
                if keys_wareh == office_equipment:
                    in_x = Office_equipment_warehouse.warehouse.index(el)
                    Office_equipment_warehouse.warehouse[in_x][office_equipment] = Office_equipment_warehouse.warehouse[in_x][office_equipment] - quantity

            add_division = {}
            add_division[office_equipment] = quantity

            dict_comp_div = {}
            dict_comp_div[company_division] = add_division

            Office_equipment_warehouse.division.append(dict_comp_div)

    @staticmethod
    def chekink_int(number):
        if type(number) == int:
            return number
        else:
            raise TypeError

    def __str__(self):
        return f'{Office_equipment_warehouse.warehouse}'

class Office_equipment():
    quantity_office_equipment = 0

    def __init__(self, stamp, model, price, id):
        self.stamo = stamp
        self.model = model
        self.price = price
        self.id = id

    @classmethod
    def __str__(cls):
        return cls.__init__()

class Printer(Office_equipment):
    Office_equipment.quantity_office_equipment += 1
    # в данный класс мы записываем следующие атрибуты марка модель цена йди, марка красок, скорость печати
    def __init__(self, stamp, model, price, id, paint_brand, paint_speed):
        self.stamp = stamp
        self.model = model
        self.price = price
        self.id = id
        self.paint_brand = paint_brand
        self.paint_speed = paint_speed

        self.tuple_atribut_object = (self.stamp, self.model, self.price, self.id, self.paint_brand, self.paint_speed)

    def __str__(self):
        return {self.stamp}, {self.model}, {self.price}, {self.id}, {self.paint_brand}, {self.paint_speed}


class Scaner(Office_equipment):
    Office_equipment.quantity_office_equipment += 1
    # в данном класе записываем марку, модель, цена, йди, скорость сканирования.
    def __init__(self, stamp, model, price, id, scaling):
        self.stamp = stamp
        self.model = model
        self.price = price
        self.id = id
        self.scaling = scaling

        self.tuple_atribut_object = (self.stamp, self.model, self.price, self.id, self.scaling)

    def __str__(self):
        return {self.stamp}, {self.model}, {self.price}, {self.id}, {self.scaling}

class Copy_shop(Office_equipment):
    Office_equipment.quantity_office_equipment += 1

    # в данный класс мы записываем следующие атрибуты марка модель цена йди, марка красок, скорость печати, скорость сканирования
    def __init__(self, stamp, model, price, id, paint_brand, paint_speed, scaling):
        self.stamp = stamp
        self.model = model
        self.price = price
        self.id = id
        self.paint_brand = paint_brand
        self.paint_speed = paint_speed
        self.scaling = scaling

        self.tuple_atribut_object = (self.stamp, self.model, self.price, self.id, self.paint_brand, self.paint_speed,
                               self.scaling)

    def __str__(self):
        return {self.stamp}, {self.model}, {self.price}, {self.id}, {self.paint_brand}, {self.paint_speed}, {self.scaling}


print_1 = Printer('Принтер samsung', 'A-320', 2500, 1, 'палитра', 1000)
#print(print_1)
scaner_1 = Scaner('Сканер samsung', 'A-100', 1500, 1, 5)
#print(scaner_1)
copy_shope_1 = Copy_shop('Ксерокс samsung', 'S2000', 8000, 1, 'palit_sam', 300, 3)
#print(copy_shope_1)

print(Office_equipment.quantity_office_equipment)

Office_equipment_warehouse.admission_warehouse(print_1.tuple_atribut_object, 5)
Office_equipment_warehouse.admission_warehouse(scaner_1.tuple_atribut_object, 5)
Office_equipment_warehouse.admission_warehouse(copy_shope_1.tuple_atribut_object, 5)

print(Office_equipment_warehouse.warehouse)

#Office_equipment_warehouse.transfer_divisions('финансы', 1, copy_shope_1.tuple_atribut_object)
Office_equipment_warehouse.transfer_divisions('бухгалтерия', 'три', scaner_1.tuple_atribut_object)
#Office_equipment_warehouse.transfer_divisions('обучения персонала', 4, print_1.tuple_atribut_object)

print(Office_equipment_warehouse.division)

print(Office_equipment_warehouse.warehouse)
