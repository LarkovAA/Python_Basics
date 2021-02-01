class Road():
    def __init__(self, length, widht):
        self._length = int(length)
        self._width = int(widht)

    def calculation_mass(self):
        WEIGHT_ASPHALT = int(input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см ? '))
        THICKNESS_ASPHALT = int(input('Введите толщину асфальта в см ? '))

        calc = (self._length * self._width * WEIGHT_ASPHALT * THICKNESS_ASPHALT) / 1000
        print(f'{calc} тонн составит масса асфальта дороги введенных вами значениях')

r_d = Road(50, 10000)

r_d.calculation_mass()