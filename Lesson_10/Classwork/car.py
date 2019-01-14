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


class Battery():
    """Простая модель аккумулятора электромобиля"""
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора"""
        self. battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("Мощность батареи данного автомобиля {} киловатт / час".format(self.battery_size))

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "Данная машина может без зарядки пройти примерно {} километров на полном заряде".format(range)
        print(message)


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса- родителя"""
        super().__init__(make, model, year)  # Похоже, что super - это ссылка на класс- родитель
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()