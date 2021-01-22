def my_func(x, y):
    degree = x ** y
    print(f'Число {x} в степени{y} равняется {degree}')

num_1 = int(input('Введите действительное положительное число? '))
num_2 = int(input('Введите целое отрицательное число? '))
if num_1 >= 0 and num_2 < 0:
    my_func(num_1, num_2)

# Вычисление степени через цикл
counter = 1
while counter <= abs(num_2):
    degree = 1 / (num_1 ** counter)
    counter += 1
print(f'Число {num_1} в степени {num_2} равняется {degree}. Вычисление через цикл')