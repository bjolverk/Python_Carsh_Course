vasilisa ={
    'name': 'vasilisa',
    'species': 'cat',
    'owner': 'irina vladimirovna'
}

tikhon= {
    'name': 'tikhon',
    'species': 'cat',
    'owner': 'anton'
}

pets = [vasilisa, tikhon]

for pet in pets:
    print(pets.index(pet) + 1)
    for category, detail in pet.items():
        print('\t{} --> {}'.format(category.upper(), detail.title()))
