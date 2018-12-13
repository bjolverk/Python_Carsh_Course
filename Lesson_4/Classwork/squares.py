squares = []
for value in range(1, 11):
    #square = value**2
    squares.append(value**2);
print(squares)

digits = list(range(1, 10))

print(type(digits))

digits.append(0)

print(type(digits))

print(digits)

print(max(digits))

print(min(digits))

print(sum(digits))

squares_new = [value**2 for value in range(0, 11)] #Генератор списка
print(squares_new)
