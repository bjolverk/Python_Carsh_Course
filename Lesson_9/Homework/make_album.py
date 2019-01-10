catalog_full =[]
def make_album(band, album, num_of_tracks=''):
    result = {'band': band, 'album':album}
    if num_of_tracks:
        result['num of tracks'] = num_of_tracks

    return result

for i in range(3):
    print('\nВведите название группы, альбома и, если есть, количество трэков')
    group_name = input("Введите название группы: ")
    album_name = input("Введите название альбома: ")
    tracks = input("Введите количество треков: ")

    music_catalog = make_album(group_name, album_name, tracks)

    print(music_catalog)

    catalog_full.append(music_catalog)

print(catalog_full)
