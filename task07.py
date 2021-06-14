def my_recurs(n):
    if n == 1:
        return n
    sum = n + my_recurs(n-1)
    return sum
n = 33
r = n*(n+1)/2
if r == my_recurs(n):
    print(True)
else:
    print(False)