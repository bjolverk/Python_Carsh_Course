import time
class User():
    """Модель пользователя"""
    def __init__(self, firstname, lastname, nicname,  group='user'):
        """Генератор пользователей"""
        self.firstname = firstname
        self.lastname = lastname
        self.nicname = nicname
        self.group = group
        self.reg_time = time.strftime('%Y%M%D')

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print("Пользователь {nic} его имя {firstname} его фамилия {lastname}, вермя регистрации {time_reg} членство в группе {membership}".format(nic = self.nicname.title(), firstname = self.firstname.title(), lastname = self.lastname.title(), time_reg = self.reg_time, membership = self.group))

    def greet_user(self):
        """Выводит персональное приветствие для пользователя"""
        print("Здравствуйте, {0} {1}, мы рады Вас видеть!".format(self.firstname, self.lastname))



larin = User("Василий", "Ларин", "Larian")

larin.describe_user()
larin.greet_user()