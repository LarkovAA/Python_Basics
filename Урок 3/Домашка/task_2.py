name = input('Введите ваше имя ? ')
surname = input('введите вашу фамилию ? ')
city_residence = input('Введите город вашего прживания ? ')
email = input('Введите ваш email ? ')
year_birth = int(input('Введите дату вашего рождения ? '))
try:
    telephone = int(input('Введите ваш телефон ? '))
except:
    print('Введите значения из чисел и слов')

def user_data(f_name = name, f_surname = surname, f_year_birth = year_birth, f_city_residence =
              city_residence, f_email = email, f_telephone = telephone ):
    print(f'{f_name} {f_surname} {f_year_birth} года рождения вы ввели следующие данные: город проживания {f_city_residence}'
          f'ваш email: {f_email} и телефон {f_telephone}')

user_data()