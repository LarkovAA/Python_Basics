class Exception():
    list_number = []
    number_attribut = ''
    @staticmethod
    def check_exception(number):
        Exception.number_attribut = number
        try:
            Exception.number_attribut = int(number)
        except:
            return print('Вы ввели не число')
        else:
            Exception.list_number.append(Exception.number_attribut)
            return Exception.list_number

input_value = None
while input_value != 'exit':
    input_value = input('Введите число. Для выхода наберите exit ')
    if input_value == 'exit':
        break
    Exception.check_exception(input_value)

print(Exception.list_number)
