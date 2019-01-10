class Restaraunt():
    """Генератор ресторанов"""
    def __init__(self, restaurant_name, cuisine_type):
        """Здесь задаются базовые параметры"""
        self.restaraunt_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Здесь выводится информация о ресторане"""
        print("Данный ресторан называется {} здесь подают блюда {} кухни".format(self.restaraunt_name.title(), self.cuisine_type))

    def open_restaurant(self):
        """Эта функция открывает ресторан"""
        print("Ресторан {} открыт! Добро пожаловать!".format(self.restaraunt_name))

blinnaya = Restaraunt('Блинная', 'русской')
blinnaya.describe_restaurant()

mcdonalds = Restaraunt('Макдональдс', 'американской')
mcdonalds.describe_restaurant()

yaposhka = Restaraunt('Япошка','японской')
yaposhka.describe_restaurant()
