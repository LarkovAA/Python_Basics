import time
class TrafficLight():
    def __init__(self, collor):
            self.__collor = list(map(lambda x: x.lower(), collor))

    def running(self):
        if self.__collor == ['красный', 'желтый', 'зеленый']:
            for el in self.__collor:
                if el == 'красный':
                    print(f'{el}')
                    time.sleep(7)
                elif el == 'желтый':
                    print(f'{el}')
                    time.sleep(2)
                elif el == 'зеленый':
                    print(f'{el}')
                    time.sleep(5)
        else:
            print('Введите правильные цвета')

t_l = TrafficLight(['красный', 'фиолетовый', 'зеленый'])

t_l.running()