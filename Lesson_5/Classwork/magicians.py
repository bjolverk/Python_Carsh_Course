magicians = ['alice', 'david', 'carolina', 'Василиса']

for magician in magicians:
    print(str(magicians.index(magician) + 1) + ' ' + magician.title() + ' that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great show!")
