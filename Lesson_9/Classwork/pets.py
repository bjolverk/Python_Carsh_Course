def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}".format(animal_type, pet_name.title()))


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willy')
