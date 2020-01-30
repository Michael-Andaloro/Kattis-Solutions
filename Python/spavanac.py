h, m = [int(x) for x in input().split()]
reverse = 45

while reverse != 0:
    if h == 0 and m == 0:
        h = 24
        m = 00
    if m == 0:
        h += -1
        m = 59
        reverse += -1
    else:
        m += -1
        reverse += -1

print(h, m)