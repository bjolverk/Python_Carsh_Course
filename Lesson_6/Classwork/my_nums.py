my_nums= [i for i in range(1, 10)]
print(my_nums)

suff=None

for num in my_nums:
    if num == 1:
        suff='st'
    elif num == 2:
        suff = 'nd'
    elif num == 3:
        suff = 'rd'
    else:
        suff = 'th'
    print('{}{}'.format(num, suff))
