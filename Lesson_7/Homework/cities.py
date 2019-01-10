cities = {
    'moscow': {
        'country': 'Russia',
        'population': 12_506_468,
        'fact': 'Тут живёт больше людей, чем во всех странах Прибалтики, вместе взятых.'
    },
    'new york': {
        'country': 'USA',
        'population':  	8_405_837,
        'fact': 'В нью-йоркском метро выявлено 12 152 формы жизни (включая насекомых и бактерии).'
    },
    'boston': {
        'country': 'USA',
        'population': 625_087,
        'fact': ' Бостон очень молодежный город'
    }

}

for city_name, city_details in cities.items():
    print('Город {}'.format(city_name.title()))
    for key, value in city_details.items():
        print('\t\t{} ---> {}'.format(key.title(), value))
