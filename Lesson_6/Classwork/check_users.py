current_users = ['Антон', 'Ксюша', 'Аня', 'Лёша', 'Вася', 'Тиша', 'Admin']
new_users = ['Вася','Петя', 'Саша', 'Миша', 'Ваня', 'Игнат', 'Антон', 'антон', 'АНТОН']

for new_name in new_users:
    flag = False
    for curr_name in current_users:
        if new_name.lower() == curr_name.lower():
            flag=True
    if flag:
        print('Имя {} занято'.format(new_name))
    else:
        print('Имя {} свободно'.format(new_name))
