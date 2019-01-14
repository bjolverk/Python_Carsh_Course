from user import User
from privileges import Privileges

class Administrator(User):
    """Модель алминистратора"""
    def __init__(self, firstname, lastname, nicname):
        """Задаёт параметры пользователя"""
        super().__init__(firstname, lastname, nicname)
        self.group = 'Administrator'
        self.plivileges = Privileges()

