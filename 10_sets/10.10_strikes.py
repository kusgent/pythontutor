# http://pythontutor.ru/lessons/sets/problems/strikes/

n, k = [int(i) for i in input().split()]
s = set()
for i in range(k):
    a, b = [int(i) for i in input().split()]
    for j in range(a, n + 1, b):
        if (j + 1) % 7 != 0 and j % 7 != 0:
            s.add(j)
print(len(s))