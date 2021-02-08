from abc import ABC, abstractmethod
# создал класс одежда
class Сlothes(ABC):
    # создаем атрибуты экземпляра имя и размер
    def __init__(self, name, clothes):
        # проверяем являеться ли имя строкой
        if type(name) == str:
            self.name = name.lower()
        else:
            raise TypeError
        self.clothes = clothes

    # создаем метот для расчета затрат ткани и указываем к нему декоратор абстрактного метода.
    @abstractmethod
    def fabric_consumption(self):
        if self.name == 'пальто':
            return ((self.clothes / 6.5) + 0.5)
        if self.name == 'костюм':
            return ((self.clothes * 2) + 0.3)
# создаем класс пальто
class Coat(Сlothes):
    # создаем словарь размеров
    sizes = {'xxs': 140, 'xs': 150, 's': 160, 'm': 170, 'l': 180, 'xl': 190, 'xxl': 200}
    def __init__(self, name, clothes):
        super().__init__(name, clothes)
        #  проверяем является атрибут экземпляра строкой или нет
        if type(self.clothes) == str:
            self.clothes = Coat.sizes[clothes]
        else:
            raise TypeError

    # добовляем декоратор проперти к методу расчета затрат
    @property
    def fabric_consumption(self):
        # опреедляем затрыты в зависимости от того что мы шьем
        if self.name == 'пальто':
            expenses = (self.clothes / 6.5) + 0.5
            return round(expenses, 2)

        if self.name == 'костюм':
            expenses = ((self.clothes * 2) + 0.3)
            return round(expenses, 2)

    # создали волшебный метот с помошью которого мы сможем просчитать сумму затрат
    def __add__(self, other):
        summ = self.fabric_consumption + other.fabric_consumption
        return summ

class Costum(Сlothes):
    @property
    def fabric_consumption(self):
        if self.name == 'пальто':
            expenses = (self.clothes / 6.5) + 0.5
            return round(expenses, 2)

        if self.name == 'костюм':
            expenses = ((self.clothes * 2) + 0.3)
            return round(expenses, 2)

    def __add__(self, other):
            summ = self.fabric_consumption + other.fabric_consumption
            return summ

c_t_1 = Coat('пальто', 'm')
c_t_2 = Coat('пальто', 'l')
c_m_1 = Costum('костюм', 170)
c_m_2 = Costum('костюм', 140)
print(c_t_1.fabric_consumption)
print(c_m_1.fabric_consumption)

print(c_t_1 + c_m_1)