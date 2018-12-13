from time import sleep as pause

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print('Adding mushrooms.')
pause(1)
if 'pepperoni' in requested_topping:
    print('Adding pepperoni.')
pause(1)
if 'extra cheese' in requested_topping:
    print('Adding extra cheese.')
pause(1)

print('\nFinished making your pizza!')
