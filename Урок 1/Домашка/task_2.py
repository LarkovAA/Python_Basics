print('Добрый день. Вы в программе переводчике времени')
# запрашиваем время в секундах
time_in_seconds = int(input('Пожалуйста введине время в секундах ? '))

time_in_hours = time_in_seconds // 3600  # определяем сколько полных часов в указаном времени
time_in_minutes = (time_in_seconds % 3600) / 60 # определяем остаток от определенных часов и высчитываем колличество минут
time_in_seconds = time_in_seconds % 60 # определяем секунды от остатка минут.
print(f'Вы ввели время {int(time_in_hours)}:{int(time_in_minutes)}:{int(time_in_seconds)}')

