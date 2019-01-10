favorite_languages ={
    'jen': ['python, ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print('{}\'s favorite languages is:'.format(name))
    for languge in languages:
        print('\t{}'.format(languge))
