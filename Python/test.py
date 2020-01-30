from sys import stdin
N = int(stdin.readline().strip())

result = 0
for i in range(0, N):
    q, p = [float(x) for x in input().split()]
    result += q * p

print(result)