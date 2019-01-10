user_size = input("Введите рвзмер Вашей футболки (S,M,L)")
user_logo = input("Ввведите текст для логотипа.")

def make_shirt(size='l', logo='I love Python'):
    avaliable_sizes = ['s', 'm', 'l', 'xl']
    if (size.lower()) in avaliable_sizes:
        print("Изготавливаю футболку размера {} с логотипом {}".format(size.upper(), logo))
    else:
        print('Ошибка, такого размера нет!')

make_shirt(user_size, user_logo)
make_shirt(size=user_size, logo=user_logo)
make_shirt()


