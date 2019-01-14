"""Класс для киосков с мороженым"""
from restaurant import Restaraunt  # На ошибку не смотрим


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

