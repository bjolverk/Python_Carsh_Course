def greet_user(first_name, last_name):
    """Выводит простое приветствие"""
    return "{} ".format(first_name.title(), last_name.title())

while True:
    print("\nПожалуйста, скажите, как Вас зовут?")
    f_name = input("Ваше имя: ")
    l_name = input("Ваша фамилия: ")

    if f_name and l_name:
        formatted_name = greet_user(f_name, l_name)
        print("Привет, " + formatted_name + "!")
    else:
        break



