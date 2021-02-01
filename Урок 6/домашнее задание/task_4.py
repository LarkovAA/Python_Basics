import random
import time
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        if type(is_police) == bool:
            self.is_police = is_police
        else:
            print('Введите булевское значение !! ')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        turn_around = ['повернул налево', 'повернул направо', 'развернулась', 'продолжает ехать вперет']
        where_turn = random.randint(0, 3)
        print(f'{self.name} {turn_around[where_turn]}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')
        if self.speed > 60:
            print('Внимание вы привысили скорость')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')
        if self.speed > 40:
            print('Внимание вы привыKсили скорость')

class PoliceCar(Car):
    pass

while True:
    t_c = TownCar(random.randint(0, 120), 'white', 'BMW', False)
    s_c = SportCar(random.randint(0, 240), 'red', 'Ferari', False)
    w_c = WorkCar(random.randint(0, 60), 'orange', 'Kamaz', False)
    p_c = PoliceCar(random.randint(0, 150), 'blue', 'Lada', True)

    all_cars = [t_c, s_c, w_c, p_c]

    for el in all_cars:
        if el.speed > 0:
            el.go()
            time.sleep(3)
            el.show_speed()
            time.sleep(3)
        elif el.speed == 0:
            el.stop()
            time.sleep(3)
        el.turn()
        time.sleep(3)