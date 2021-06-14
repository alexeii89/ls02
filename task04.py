def myrecurs(n, i):
    if n == 1:
        return i
    sum_a = i  + myrecurs(n-1, i / -2)
    return sum_a
print(myrecurs(4, 1))