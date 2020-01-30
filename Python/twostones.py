from sys import stdin

N = int(stdin.readline().strip())

# Odd = Alice; Even = Bob

while N > 2:
	N += -2

if N == 2:
	print("Bob")
else:
	print("Alice")