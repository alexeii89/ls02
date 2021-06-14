
def ascii(st, end):
    print("%4d - %s " % (st, chr(st)), end='')
    if (end + st - 158) % 10 == 0:
        print()
    if st == end:
        return True
    ascii(st+1, end)
ascii(32, 127)