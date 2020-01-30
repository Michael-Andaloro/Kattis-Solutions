from sys import stdin

N = int(stdin.readline().strip())

for i in range(0, N):
	x = int(stdin.readline().strip())
	if x % 2 == 0:
		print(str(x) + " is even")
	else:
		print(str(x) + " is odd")