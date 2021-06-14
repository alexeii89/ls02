import random

even = 0


def ugadayka(n):
    global even
    r = int(input('Отгадайте число от 0 до 99: '))
    if r == n:
        return print(f"Поздравляем вы отгадали число {n}")
    elif r > n:
        print(f'число меньше {r}')
    elif r < n:
        print(f'число больше {r}')
    even += 1
    if even == 10:
        return print(f'вы проиграли загаданое число было {n}')
    ugadayka(n)


n = random.randint(0, 99)
ugadayka(n)
