# создаем класс матрицу
class Matrix():
    def __init__(self, matrix):
        # проверяем являеться тип введеных данных списком
        if type(matrix) == list:
            self.matrix = matrix
        else:
            raise ValueError('Введите матрицу ввиде списков')

    def __str__(self):
        return f'Получившаяся матрица {self.matrix}'

    def __add__(self, other):
        # проверяем имеют ли матрицы одинаковое колличество строков и столбцов
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            # создаем списко куда записываем результаты слодения каждого элемента
            summ_matrixs = []
            # с помошью цикла фор проходим по строкам матрицы
            for el_summ in range(len(self.matrix)):
                # присваиваем элементы строк 2-м переменным
                s_matrix = self.matrix[el_summ]
                o_s_matrix = other.matrix[el_summ]
                try:
                    summ_matrixs.append(summ_el)
                except:
                    pass
                # создаем список в котором запишем результаты сложения каждой строчки
                summ_el = []
                #  с помошью цикла фор проходим по столбцам каждой строчки
                for el in range(len(self.matrix[el_summ])):
                    summ = s_matrix[el] + o_s_matrix[el]
                    summ_el.append(summ)
                if el_summ == (len(self.matrix) - 1):
                    summ_matrixs.append(summ_el)
            return summ_matrixs
        else:
            return print('Вы суммируете матрицы разных размеров !!')

mat_1 = Matrix([[1,2,3], [4,5,6,], [7,8,9]])
mat_2 = Matrix([[1,2,3], [4,5,6,]])
print(mat_1)
print(mat_2)
print(mat_1 + mat_2)


