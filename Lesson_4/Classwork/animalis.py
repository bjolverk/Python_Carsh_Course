from time import sleep as pause
mammals = ['dog', 'cat', 'rat', 'hamster', 'ferret']

for pet in mammals:
    print("A {} would be a great pet".format(pet.title()))
    pause(1)
print("Any of these animals would make a great pet!")
