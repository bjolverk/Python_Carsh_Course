alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print('Original x_position {}'.format(alien_0['x_position']))

# Пришелец смещается вправо
# Вычисляем величину на основании текущей скорости

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3

# Новая позиция равна сумме старой позиции и приращения


alien_1 ={
    'color': 'red',
    'points': 15,
    'x_position': 0,
    'y_position': 25,
    'speed': 'high'
}

print(alien_1)