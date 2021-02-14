class Complex_number():
    def __init__(self, number):
        if type(number) == complex:
            self.com_num = number
        else:
            print('Вы ввели не комплексное число')

    def __str__(self):
        return self.com_num

    def __add__(self, other):
        return self.com_num + other.com_num

    def __mul__(self, other):
        return self.com_num * other.com_num

num_1 = Complex_number(3 + 5J)
num_2 = Complex_number(17 + 0.25j)

print(num_1 + num_2)
print(num_1 * num_2)