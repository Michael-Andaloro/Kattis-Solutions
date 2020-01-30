from sys import stdin

initial = int(stdin.readline().strip())
N = int(stdin.readline().strip())
data = initial

for i in range(0,N):
	usage = int(stdin.readline().strip())
	data += initial - usage

print(data)