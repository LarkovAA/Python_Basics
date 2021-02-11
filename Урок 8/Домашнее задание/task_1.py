# создаем словарь с ключем месяц и значением числом который означает этот месяц
dictionary_months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
                     'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
# создаем метод для проверки введенных значений дат
def checking_date(num_max, num_min, variable):
    # если атрибут класса больше мин значения и меньше максимального то оставляем атрибут без изменений
    if num_max <= variable >= num_min:
        variable = variable
    # если атрибут больше максимального значения то атрибуту присваиваем максимальное значение
    if variable > num_max:
        variable = num_max
    # если атрибут меньше минимального значения то присваиваем минимальное значение
    if variable < num_min:
        variable = num_min
    return variable
# создаем класс даты
class Date:
    def __init__(self, date_str):
        self.date = date_str

   # создаем декоратор класс метод который переводит значения в число
    @classmethod
    def convert_number(cls, date):
        # создаем список с поошьюметода сплит разбиваем получение значения через -
        list_date = date.split('-')
        try:
            # добавляем в атрибут класса получившийся список при этом с помошью мар меняяем тип элементов списка с строки на числа
            # в случае ощибки если строку нельзя преобразовать в число
            cls.date_str = list(map(int, list_date))
        except:
            #  мы предполагаем что пользователь ввел месяц в формате строки тогда мы с помошью словаря по ключю находим значение того месяца который указан и находим в словаре его значение.
            list_date[1] = dictionary_months[list_date[1]]
            # по новой переводим элементы списка в тип данных число
            cls.date_str = list(map(int, list_date))
        return cls.date_str

    @staticmethod
    # с помошью статикметода создаем метод класса который определит коректность введенных данных
    def validation():
        # в цикле фор проходим всю длинну списка атрибута класса date_str
        for el in range(0, len(Date.date_str)):
            # проверяем первый элемент списка атрибута класса через фукцию checking_date
            if el == 0:
                number = checking_date(31, 1, Date.date_str[el])
                Date.date_str[el] = number
            if el == 1:
                number = checking_date(12, 1, Date.date_str[el])
                Date.date_str[el] = number
            if el == 2:
                return Date.date_str

    def __str__(self):
        return Date.date_str

print(Date.convert_number('-2-15-1993'))
print(Date.validation())
