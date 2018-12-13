from time import sleep as pause
names = ['Антон', 'Ксюша', 'Аня', 'Лёша', 'Вася', 'Тиша', 'Admin']
names=[]

if names:
    for name in names:
        if name == 'admin' or name == 'Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Привет {} спасибо, что залогинились'.format(name))

        pause(5)
else:
    print('Надо кого- нибудь найти!')
