def greet_users(names):
    """Вывод простого приветствия для каждого человека в списке"""
    for name in names:
        msg = "Hello, {}!".format(name.title())
        print(msg)


usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)
