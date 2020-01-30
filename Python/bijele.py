given = list(map(int, input().split(' ')))
correct = [1, 1, 2, 2, 2, 8]

adjust = [x1 - x2 for (x1, x2) in zip(correct, given)]

print (" ".join([str(x) for x in adjust]))