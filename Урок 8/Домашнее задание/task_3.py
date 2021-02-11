class Exception():
    number_str = None
    @staticmethod
    def check_exception(number):
        try:
            number = int(number)
        except:
            pass
        else:
            Exception.number_strmber = number
            return Exception.number_strmber

input_value = None
list_number = []
while input_value != 'exit':
    input_value = input('Введите число. Для выхода наберите exit ')
    if input_value == 'exit':
        break
    list_number.append(Exception.check_exception(input_value))

print(list_number)
