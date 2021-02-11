# создаем класс
class Exception():
    # в атрибутах класса записываем список в который мы запишем все полученные элементы и переменную которую будем добавлять в список
    list_number = []
    number_attribut = ''

    # создаем статикметод который будет проверять являеться ли ввоодимые данные числами
    @staticmethod
    def check_exception(number):
        Exception.number_attribut = number
        # проверяем являеться ли введеные данные числом
        try:
            Exception.number_attribut = int(number)
        # если нет то выводим ошибку
        except:
            return print('Вы ввели не число')
        # если ошибки не возникает мы добавляем в список данное число
        else:
            Exception.list_number.append(Exception.number_attribut)
            return Exception.list_number

# создаем переменную в которую будем записывать введенные данные
input_value = None
# создаем цикл который будет работать пока переменная не примет значение exit
while input_value != 'exit':
    input_value = input('Введите число. Для выхода наберите exit ')
    if input_value == 'exit':
        break
    Exception.check_exception(input_value)

print(Exception.list_number)
