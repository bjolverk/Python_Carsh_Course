my_foods = ['pizza', 'falafel', 'carrot cake', 'sushi', 'Big Mac', 'Big tasty', 'Free potato']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are: ')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)
print('The first three items in the list are:')
for i in my_foods[:3]:
    print(i)

print('Three items in the middle of the list are:')
for i in my_foods[int(len(my_foods)/2)-1:int(len(my_foods)/2)+2]:
    print(i)

print('The last three items in the list are:')
for i in my_foods[-3:]:
    print(i)
