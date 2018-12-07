motorcycles = ['Honda CBR250R', 'Ducati Desert Sled', 'Yamaha YZF-R3',
'Kawasaki Versys-X 300', 'Honda Rebel 300', '2017 Triumph Street Scrambler']

for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))

print("=*=" * 50)

motorcycles.append('Yamaha Star Bolt R-Spec')

for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))
print("=*=" * 50)
motorcycles.insert(-2, 'URAL WOLF')

for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))
print("=*=" * 50)
del motorcycles[0]

for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))
print("=*=" * 50)

popped_motorcycle = motorcycles.pop()

for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))
print(popped_motorcycle)
print("=*=" * 50)

first_owned = motorcycles.pop(0)
print(first_owned)
for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))
print("=*=" * 50)

motorcycles.remove('URAL WOLF')

for i in range(len(motorcycles)):
    print("i would like to buy {} motorcycle".format(motorcycles[i]))
print("=*=" * 50)
