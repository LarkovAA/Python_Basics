dict_income = {'оклад': None, 'премия': None}

class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self, salary, premium):
        self._income['оклад'] = salary
        self._income['премия'] = premium

        sum_income = sum(list(self._income.values()))
        print(f'{sum_income} такую запрлату имеет данный сотрудник')


pos_on = Position('Алексей', 'Ларьков', 'програмист', dict_income)

pos_on.get_full_name()
pos_on.get_total_income(30000, 15000)


