from sys import stdin

name = str(stdin.readline().strip())
count = 0

for i in name: 
    if i == '-': 
        count = count + 1
names = []
for i in range(0,count+1):
    names.append(name.rsplit("-", count)[i])
short = ""
for j in range(0, len(names)):
    temp = names[j]
    short += temp[:1]
print(short)