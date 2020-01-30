from sys import stdin
import math

n, w, h = [int(x) for x in input().split()]

maximum = math.sqrt((w*w+h*h))

for i in range(0, n):
	l = int(stdin.readline().strip())
	if l <= maximum:
		print("DA")
	else:
		print("NE")