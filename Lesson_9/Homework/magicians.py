magicians = ['Alice', 'Markus', 'Salazar']

def show_magicians(mag_list):
    """Выводим список фокусников"""
    for maician in mag_list:
        print(maician)


def make_great(mag_list):
    """Делаем фокусника вновь великим"""
    inner_list=[]
    for i in range(len(mag_list)):
        inner_list.append(mag_list[i] + ' великий!')
    return inner_list




show_magicians(make_great(magicians))
show_magicians(magicians)