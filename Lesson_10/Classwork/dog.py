class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты имени и возраста"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится"""
        print(self.name.title() + " is now sitting")

    def roll(self):
        """Собака перекатывается по команде"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('Люси', 3)
print("Мою собаку зовут {}".format(my_dog.name.title()))
print("Моей собаке {} лет".format(my_dog.age))
my_dog.sit()
my_dog.roll()

print("Твою собаку зовут {}".format(your_dog.name.title()))
print("Твоей собаке {} лет.".format(your_dog.age))


