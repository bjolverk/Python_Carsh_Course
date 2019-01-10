def make_pizza(size, *toppings):
    """Выводим описание пиццы"""
    print('\nДелаем {}-ую пиццу со следующими топпингами:'.format(size))
    for topping in toppings:
        print('\t-{}'.format(topping))

# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')
