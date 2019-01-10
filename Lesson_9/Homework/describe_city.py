def describe_sity(city_name='Рейкьявик', country_name='Исландия'):
    print("Город {} расположен в стране {}".format(city_name.lower().title(), country_name.lower().title()))

describe_sity('Москва', 'Россия')
#describe_sity('', '')
describe_sity('Осло', 'Новрегия')
describe_sity()
