import time
class User():
    """Модель пользователя"""
    def __init__(self, firstname, lastname, nicname, group='user'):
        """Генератор пользователей"""
        self.firstname = firstname
        self.lastname = lastname
        self.nicname = nicname
        self.group = group
        self.reg_time = time.strftime('%Y%M%D')
        self.login_attempts = 0

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print("Пользователь {nic} его имя {firstname} его фамилия {lastname}, вермя регистрации {time_reg} членство в группе {membership}".format(nic = self.nicname.title(), firstname = self.firstname.title(), lastname = self.lastname.title(), time_reg = self.reg_time, membership = self.group))

    def greet_user(self):
        """Выводит персональное приветствие для пользователя"""
        print("Здравствуйте, {0} {1}, мы рады Вас видеть!".format(self.firstname, self.lastname))

    def show_user_attempts(self):
        """Показывает количество попыток входа"""
        print("Пользователь {} совершил {} попыток входа в систему".format(self.nicname, self.login_attempts))

    def increment_login_attempts(self):
        """Увеличивает количество попыток входа"""
        self.login_attempts += 1

    def reset_user_attempts(self):
        self.login_attempts = 0


class Privileges():
    """Класс определяет привилегии админа"""
    def __init__(self):
        self.privileges = privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        for item in self.privileges:
            print("\t-{}".format(item))


class Administrator(User):
    """Модель алминистратора"""
    def __init__(self, firstname, lastname, nicname):
        """Задаёт параметры пользователя"""
        super().__init__(firstname, lastname, nicname)
        self.group = 'Administrator'
        self.plivileges = Privileges()


#larin = Administrator("Василий", "Ларин", "Larian")
#larin.plivileges.show_privileges()

