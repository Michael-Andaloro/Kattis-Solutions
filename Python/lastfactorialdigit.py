from sys import stdin

N = int(stdin.readline().strip())

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  

for i in range(0, N):
	x = int(stdin.readline().strip())
	fact = factorial(x)
	print(fact%10)