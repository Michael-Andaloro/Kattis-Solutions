from sys import stdin

num = int(stdin.readline().strip())
temp = list(map(int, input().split(' ')))
answer = 0

i = 0
while i < num:
    if temp[i] < 0:
        answer += 1
    i += 1
    
print(answer)