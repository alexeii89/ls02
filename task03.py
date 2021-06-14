def myrecurs(el):
    if len(str(el)) == 1:
        return str(el)
    else:
        r = str(el % (el//10 * 10)) + str(myrecurs(el//10))
    return r
print(myrecurs(123080950))