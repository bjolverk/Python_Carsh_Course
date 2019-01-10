from mimesis import Person
import random

prsons = {}

for i in range(10):
    person = Person('pl').full_name()
    prsons[person] = []
    user_nums=[]
    for i in range(6):
        user_nums.append(random.randint(1, 10))
    prsons[person].extend(list(set(user_nums)))




for human, number in prsons.items():
    print(human)
    for i in number:
        print('\t {}'.format(i))
