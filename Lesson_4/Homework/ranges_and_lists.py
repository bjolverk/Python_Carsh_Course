odd = list(range(1, 21, 2))

for i in odd:
    print(i)
print('=*=' * 50)
new_list = list(range(3, 31, 3))

for i in new_list:
    print(i)
print('=*=' * 50)
cubes_old=[]
for i in range(1, 11):
    cubes_old.append(i**3)

for i in cubes_old:
    print(i)
print('=*=' * 50)

cubes = [i**3 for i in range(1,11)]

for i in cubes:
    print(i)
