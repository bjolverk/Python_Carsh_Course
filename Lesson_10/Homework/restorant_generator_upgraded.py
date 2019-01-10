class Restaraunt():
    """Генератор ресторанов"""
    def __init__(self, restaurant_name, cuisine_type):
        """Здесь задаются базовые параметры"""
        self.restaraunt_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Здесь выводится информация о ресторане"""
        print("Данный ресторан называется {} здесь подают блюда {} кухни".format(self.restaraunt_name.title(), self.cuisine_type))

    def open_restaurant(self):
        """Эта функция открывает ресторан"""
        print("Ресторан {} открыт! Добро пожаловать!".format(self.restaraunt_name))

    def show_number_served(self):
        print("Всего обслужено {} клиентов".format(self.number_served))

    def set_number_served(self, people_count):
        """Задаёт количество обслуженных людей"""
        if people_count > self.number_served:
            self.number_served = people_count
        else:
            print("Так нельзя!")

    def increment_number_serverd(self, clients_num):
        """Задаёт прирашение для количества клиентов"""
        if clients_num > 0:
            self.number_served += clients_num
        else:
            print("Так нельзя!")


blinnaya = Restaraunt('Блинная', 'русской')
blinnaya.describe_restaurant()
blinnaya.set_number_served(50)
blinnaya.show_number_served()

mcdonalds = Restaraunt('Макдональдс', 'американской')
mcdonalds.describe_restaurant()

yaposhka = Restaraunt('Япошка','японской')
yaposhka.describe_restaurant()
