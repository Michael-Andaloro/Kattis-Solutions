from sys import stdin

moves = str(stdin.readline().strip())
pos = ["x","y","z"]
for i in moves:
	if i == "A":
		pos[0],pos[1] = pos[1], pos[0]
	if i == "B":
		pos[1],pos[2] = pos[2], pos[1]
	if i == "C":
		pos[0],pos[2] = pos[2], pos[0]
print(pos.index("x")+1)