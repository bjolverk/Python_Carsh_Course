"""Класс для преставления автомобиля"""
class Car:  # И так тоже можно!
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = "{} {} {}".format(self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        """Выводит текущий пробег машины в милях"""
        print("Текущий пробег машины составляет {} миль".format(self.odometer_reading))

    def update_odometer(self, mileage):
        """Задаёт новое значение одометру, метод снабжён защитой от махинаций"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Значение одометра скручивать нельзя!")

    def increment_odometer(self, miles):
        """Увеличивает пробег машины с заданным приращением"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Значение одометра скручивать нельзя!")


