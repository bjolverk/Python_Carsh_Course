pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print('Вы заказали {} пиццу со следующими топпингами: '.format(pizza['crust']))
for topping in pizza['toppings']:
    print('\t'+topping)
