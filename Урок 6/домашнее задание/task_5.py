class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    
    def draw(self):
        print(f'Вы запустили отрисовку {self.title} ')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} такую отрисовку вы запустили')


class Handle(Stationery):

    def draw(self):
        print(f'Отрисовка запушена {self.title} ')

p_n = Pen('Ручка')
p_il = Pencil('карандаш')
h_le = Handle('Маркер')

list_stationery = [p_n, p_il, h_le]

for el in list_stationery:
    el.draw()
