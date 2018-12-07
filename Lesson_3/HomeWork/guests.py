my_guest_list = ['Galadriel', 'Gandalf', 'Frodo']

for i in range(len(my_guest_list)):
    print("Hello, {}! I'm inviting you to dinner.".format(my_guest_list[i]))

print(my_guest_list[len(my_guest_list) - 1] + ' Can\'t come.')

my_guest_list[2] = 'Harry Drezden'

for i in range(len(my_guest_list)):
    print("Hello, {}! I'm inviting you to dinner.".format(my_guest_list[i]))

print("we are expanding the list of invitees")

for i in range(len(my_guest_list)):
    print(my_guest_list[i])

my_guest_list.insert(0, 'Popeye the Sailor')

print('=*=' * 50)

for i in range(len(my_guest_list)):
    print(my_guest_list[i])

print('=*=' * 50)

my_guest_list.insert(int(len(my_guest_list) / 2), 'Ctulhu')

for i in range(len(my_guest_list)):
    print(my_guest_list[i])

print('=*=' * 50)

my_guest_list.append('Darth Vader')

for i in range(len(my_guest_list)):
    print("Hello, {}! I'm inviting you to dinner.".format(my_guest_list[i]))

print("I invite {} guests".format(len(my_guest_list)))

print('I think I can invite only two characters for lunch!')

while len(my_guest_list) > 2:
    print('Sorry ' + my_guest_list.pop() + ' my table is too small for a big company')

for i in range(len(my_guest_list)):
    print("Hello, {}! I'm inviting you to dinner.".format(my_guest_list[i]))

del my_guest_list[0]
del my_guest_list[0]

print(my_guest_list)
