aliens = []

for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)



#for i in range(0, len(aliens)):
#    if i >0 and i % 2 == 0:
#        aliens[i]['color'] = 'red'
#        aliens[i]['speed'] = 'high'
#        aliens[i]['points'] = 10

#for alien in aliens[::2]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


for alien in aliens[:5]:
    print(alien)
print('...')

for alien in aliens[::3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for i in aliens:
    print(i)
