# Введите первое число
# Введите операцию
# Введите 2 число
def myrecurs():
    op = input('Введите операцию (+, -, *, /) или 0 для выхода: ')
    if op == '0':
        return 'Bye!'
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if op == '*':
        print(f'{a} * {b} = {a * b}')
    elif op == '/':
        try:
            print(f'{a} / {b} = {a / b}')
        except ZeroDivisionError:
            print('На ноль келить нельзя')
    elif op == '+':
        print(f'{a} + {b} = {a + b}')
    elif op == '-':
        print(f'{a} - {b} = {a - b}')
    else:
        print('Error!')
    myrecurs()
print(myrecurs())