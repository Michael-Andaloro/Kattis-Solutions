from sys import stdin

N = int(stdin.readline().strip())

for i in range(0, N):
	M = int(stdin.readline().strip())
	cities = []
	for i in range(0,M):
		city = str(stdin.readline().strip())
		cities.append(city)
	sort = list(set(cities))
	print(len(sort))