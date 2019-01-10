favorite_places = {
    'Anton': ['Ново- Переделкино', 'Крым', 'Прага', 'Бойница'],
    'Ksenia': ['Владикавказ', 'Вилково', 'Нескучный сад']
}

for person, palces in favorite_places.items():
    print('Любимые места ' + person )
    for place in palces:
        print('\t-' + place)

