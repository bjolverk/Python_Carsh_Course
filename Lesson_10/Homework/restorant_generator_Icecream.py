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


class IceCreamStand(Restaraunt):
    """Модель киоска с мороженым"""
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):  # Именно ТАК!!!
        """Инициализируем параметры киоска"""
        super().__init__(restaurant_name, cuisine_type)
        try:
            assert flavors, 'Ok'
        except AssertionError:
            print("Без списка видов мороженного кафе не открыть. Абыдна, да?")

        self.flavors = flavors

    def describe_flavors(self):
        print('Доступны следующие сорта мороженого: ')
        for flavor in self.flavors:
            print("\t-{}".format(flavor))



# blinnaya = Restaraunt('Блинная', 'русской')
# blinnaya.describe_restaurant()
# blinnaya.set_number_served(50)
# blinnaya.show_number_served()
#
# mcdonalds = Restaraunt('Макдональдс', 'американской')
# mcdonalds.describe_restaurant()
#
# yaposhka = Restaraunt('Япошка','японской')
# yaposhka.describe_restaurant()
flavor_list = ['Blue Moon', 'Avocado ice cream', 'Butterscotch ice cream', 'Tin Roof ice cream']
morozhenka = IceCreamStand('Мороженка', 'Мороженое', flavor_list)
morozhenka.describe_restaurant()
morozhenka.describe_flavors()
