sandwich_orders = [
    'летний',
    'пастрами',
    'клубный',
    'пастрами',
    'с мясными шариками',
    'пастрами',
    'огуречный'
]

finished_sandwiches=[]

while 'пастрами' in sandwich_orders:

    sandwich_orders.remove('пастрами')

print('Внимание! Сэндвичи с пастрами кончились!')
while sandwich_orders:
    current_asndwich = sandwich_orders.pop()
    print('Я сделал сэндвич "{}"'.format(current_asndwich.title()))

    finished_sandwiches.append(current_asndwich)
for sandwich in finished_sandwiches:
    print(sandwich)
