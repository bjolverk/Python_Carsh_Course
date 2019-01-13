"""Набор классов для представления электромобилей"""
from car import Car
class Battery():
    """Простая модель аккумулятора электромобиля"""
    def __init__(self, battery_size=70):
        """Инициализация параметров аккумулятора"""
        self.battery_size = battery_size

    def describe_battery_size(self):
        """Отображат информацию о мощности аккумулятора"""
        print("Мощность аккумулятора данной машины составляет {} квт./ч".format(self.battery_size))

    def get_range(self):
        """Выводит примерный запас хода для аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "Данная машина может проехать приблизительно {} миль на полном заряде аккумулятора".format(range)
        print(message)


class ElectricCar(Car):
    """Представляет аспекты машины, характерные для электромобиля"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса- родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

