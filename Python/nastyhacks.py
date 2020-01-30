from sys import stdin

N = int(stdin.readline().strip())

for i in range(0, N):
	r, e, c = [float(x) for x in input().split()]
	incwith = e - c
	incwithout = r
	if incwithout == incwith:
		print("does not matter")
	if incwithout > incwith:
		print("do not advertise")
	if incwithout < incwith:
		print("advertise")