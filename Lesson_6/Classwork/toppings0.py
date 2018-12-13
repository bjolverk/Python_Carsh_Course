from time import sleep as pause

avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding {}".format(requested_topping))
    else:
        print("Sorry, we don't have {}".format(requested_topping))
    pause(2)
print("\nFinished making your pizza")
