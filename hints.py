For reading multiple inputs in a single line:
q, p = [float(x) for x in input().split()]

To put it all into a list right away
temp = list(map(int, input().split(' ')))

For reading multiple lines of input:
from sys import stdin

x = int(stdin.readline().strip())
y = int(stdin.readline().strip())
