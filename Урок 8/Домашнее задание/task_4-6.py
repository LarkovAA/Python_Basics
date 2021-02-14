import random
# создаем класс склад орг техники
class Office_equipment_warehouse():
    # создаем списки в которые будем записывать созданные объекты орг техники и их колличество какое было переведено на склад или в подразделения
    warehouse = []
    division = []
    list_id = []

    # создем метод класса в который будем записывать какую орг технику мы отправили на склад
    @staticmethod
    def admission_warehouse(office_equipment, quantity):
        # проверяем не являеться ли введенное значение строкой
        try:
            Office_equipment_warehouse.chekink_int(quantity)
        except:
            return print('Колличество техники вы ввели не числом а строкой')
        else:
            dic_admis_wareh = {}
            dic_admis_wareh[office_equipment] = quantity
            Office_equipment_warehouse.warehouse.append(dic_admis_wareh)

    # создаем метод класса с помошью которого мы переводим технику со склада в отделы.
    @staticmethod
    def transfer_divisions(company_division, quantity, office_equipment):
        try:
            Office_equipment_warehouse.chekink_int(quantity)
        except:
            return print('Колличество техники вы ввели не числом а строкой')
        else:
            #  спомошью цикла фор мы прверяем элементы списка warehouse
            for el in Office_equipment_warehouse.warehouse:
                # создаем переменную в которую записываем ключ по каждому циклу
                keys_wareh = tuple(el.keys())[0]
                # если ключ имеет одинаковое значение со значение той орг техники которую хотим перевести
                if keys_wareh == office_equipment:
                    # ищим индек этого элемента в списке
                    in_x = Office_equipment_warehouse.warehouse.index(el)
                    # меняем значение словаря из списка склад уменьшаем на то количество техники которую переводим в другой отдел
                    Office_equipment_warehouse.warehouse[in_x][office_equipment] = Office_equipment_warehouse.warehouse[in_x][office_equipment] - quantity
            # создаем словарь в оторый будет значение для другого словаря который будет отражать в какой отдел какую технику и сколько перенесли
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

class Office_equipment():
    quantity_office_equipment = 0

    def __init__(self, stamp, model, price):
        self.stamo = stamp
        self.model = model
        self.price = price
        while True:
            self.id = int(random.randint(1000, 9999))
            if self.id not in Office_equipment_warehouse.list_id:
                Office_equipment_warehouse.list_id.append(self.id)
                break

class Printer(Office_equipment):
    Office_equipment.quantity_office_equipment += 1
    # в данный класс мы записываем следующие атрибуты марка модель цена йди, марка красок, скорость печати
    def __init__(self, stamp, model, price, paint_brand, paint_speed):
            self.price = price
            self.paint_speed = paint_speed
            self.stamp = stamp
            self.model = model
            self.paint_brand = paint_brand
            while True:
                self.id = int(random.randint(1000, 9999))
                if self.id not in Office_equipment_warehouse.list_id:
                    Office_equipment_warehouse.list_id.append(self.id)
                    break
            self.tuple_atribut_object = (self.stamp, self.model, self.price, self.id, self.paint_brand, self.paint_speed)


class Scaner(Office_equipment):
    Office_equipment.quantity_office_equipment += 1
    # в данном класе записываем марку, модель, цена, йди, скорость сканирования.
    def __init__(self, stamp, model, price, scaling):
        self.stamp = stamp
        self.model = model
        self.price = price
        self.scaling = scaling
        while True:
            self.id = int(random.randint(1000, 9999))
            if self.id not in Office_equipment_warehouse.list_id:
                Office_equipment_warehouse.list_id.append(self.id)
                break
        self.tuple_atribut_object = (self.stamp, self.model, self.price, self.id, self.scaling)


class Copy_shop(Office_equipment):
    Office_equipment.quantity_office_equipment += 1

    # в данный класс мы записываем следующие атрибуты марка модель цена йди, марка красок, скорость печати, скорость сканирования
    def __init__(self, stamp, model, price, paint_brand, paint_speed, scaling):
        self.stamp = stamp
        self.model = model
        self.price = price
        self.paint_brand = paint_brand
        self.paint_speed = paint_speed
        self.scaling = scaling
        self.id = None
        while True:
            self.id = int(random.randint(1000, 9999))
            if self.id not in Office_equipment_warehouse.list_id:
                Office_equipment_warehouse.list_id.append(self.id)
                break

        self.tuple_atribut_object = (self.stamp, self.model, self.price, self.id, self.paint_brand, self.paint_speed,
                               self.scaling)

print_1 = Printer('Принтер samsung', 'A-320', 2500, 'палитра', 1000)
#print(print_1)
scaner_1 = Scaner('Сканер samsung', 'A-100', 1500, 5)
#print(scaner_1)
copy_shope_1 = Copy_shop('Ксерокс samsung', 'S2000', 8000, 'palit_sam', 300, 3)
#print(copy_shope_1)

print(Office_equipment.quantity_office_equipment)

Office_equipment_warehouse.admission_warehouse(print_1.tuple_atribut_object, 5)
Office_equipment_warehouse.admission_warehouse(scaner_1.tuple_atribut_object, 5)
Office_equipment_warehouse.admission_warehouse(copy_shope_1.tuple_atribut_object, 5)

print(Office_equipment_warehouse.warehouse)

Office_equipment_warehouse.transfer_divisions('финансы', 1, copy_shope_1.tuple_atribut_object)
Office_equipment_warehouse.transfer_divisions('бухгалтерия', 3, scaner_1.tuple_atribut_object)
Office_equipment_warehouse.transfer_divisions('обучения персонала', 4, print_1.tuple_atribut_object)

print(Office_equipment_warehouse.division)

print(Office_equipment_warehouse.warehouse)

print(Office_equipment_warehouse.list_id)