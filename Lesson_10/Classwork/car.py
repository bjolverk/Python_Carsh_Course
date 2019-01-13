"""Класс для преставления автомобиля"""
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = "{} {} {}".format(self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег автомобиля в милях"""
        print("Эта машина имеет пробег равный {} миль".format(self.odometer_reading))

    def update_odometer(self, mileage):
        """
        Устанавливает значение одометра
        При попытке скруток изменений не будет
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скручивать одометр")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра на заданное количество миль"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Так нельзя")

