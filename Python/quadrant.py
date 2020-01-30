from sys import stdin
x = int(stdin.readline().strip())
y = int(stdin.readline().strip())
if x > 0 and y > 0:
    print("1")
if x < 0 and y > 0:
    print("2")
if x < 0 and y < 0:
    print("3")
if x > 0 and y < 0:
    print("4")