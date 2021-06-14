even = 0
noteven = 0


def myrecurs(el):
    if int(el[0]) % 2 == 0:
        global even
        even += 1
    else:
        global noteven
        noteven += 1
    if len(el) == 1:
        return even, noteven
    return myrecurs(el[1:])


myrecurs('0123456789')
print(f'четные {even}, не четные {noteven}')
