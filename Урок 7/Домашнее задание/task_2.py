from abc import ABC, abstractmethod

class Сlothes(ABC):
    def __init__(self, name, clothes):
        if type(name) == str:
            self.name = name.lower()
        else:
            raise TypeError
        self.clothes = clothes

    @abstractmethod
    def fabric_consumption(self):
        if self.name == 'пальто':
            return ((self.clothes / 6.5) + 0.5)
        if self.name == 'костюм':
            return ((self.clothes * 2) + 0.3)

class Coat(Сlothes):
    sizes = {'xxs': 140, 'xs': 150, 's': 160, 'm': 170, 'l': 180, 'xl': 190, 'xxl': 200}
    def __init__(self, name, clothes):
        super().__init__(name, clothes)
        if type(self.clothes) == str:
            self.clothes = Coat.sizes[clothes]
        else:
            raise TypeError

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