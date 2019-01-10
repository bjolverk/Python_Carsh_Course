from mimesis import Person

peoples= []
for i in range(5):
    name = Person('ru').name()
    age = Person('ru').age(15, 54)
    occupation = Person('ru').occupation()
    peoples.append({'name': name, 'age': age, 'occupatiom': occupation})

for person in peoples:
    for item_name, item in person.items():
        print(item_name, item)
    print('=*='*30)
