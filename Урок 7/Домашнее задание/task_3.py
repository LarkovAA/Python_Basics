class Cell():
    def __init__(self, number_cell):
        self.number_cell = number_cell

    def make_orde(self, num_meshs):
        # в переменную записываем то количество количество клеток которое передаем при создании объекта
        num_cells = '*' * self.number_cell
        # переводим строку в список
        num_cells = list(num_cells)
        # определяем количество переносов которые хотим добавить
        num_mesh = int(round(self.number_cell / num_meshs, 0))
        # опеределяем на какую позицию мы утанавливаем переносы
        insert_num_mens = int(self.number_cell / num_mesh)

        for el in range(1, num_mesh + 1):
            # если количество переносов меньше или равно 1 и если количество клеток меньше чем размер ячеек
            if num_mesh <= 1 and self.number_cell <= num_meshs:
                num_cells.append('\n')
            # если количество переносов меньше или равно 1 и если количество клеток больше чем размер ячеек
            if num_mesh <= 1 and self.number_cell >= num_meshs:
                num_cells.insert(el * num_meshs, '\n')
            if num_mesh > 1:
                if el == 1:
                    num_cells.insert(el * insert_num_mens, '\n')
                if el > 1:
                    num_cells.insert(el * insert_num_mens + el - 1, '\n')

        num_cells = ' '.join(num_cells)
        return num_cells

    def __add__(self, other):
        return self.number_cell + other.number_cell

    def __sub__(self, other):
        return self.number_cell - other.number_cell

    def __mul__(self, other):
        return self.number_cell * other.number_cell

    def __truediv__(self, other):
        return round(self.number_cell / other.number_cell, 0)


a = Cell(35)
print(a.make_orde(5))
b = Cell(10)
print(b.make_orde(11))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
