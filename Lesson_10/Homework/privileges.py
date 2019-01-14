class Privileges():
    """Класс определяет привилегии админа"""
    def __init__(self):
        self.privileges = privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        for item in self.privileges:
            print("\t-{}".format(item))

