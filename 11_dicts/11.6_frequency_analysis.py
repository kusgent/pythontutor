# http://pythontutor.ru/lessons/dicts/problems/frequency_analysis/

n = int(input())
d = {}
for i in range(n):
    s = input().split()
    for elem in s:
        d[elem] = d.get(elem, 0) + 1
l = []
for key, value in d.items():
    l.append([value, key])
l = sorted(l, reverse=True)
for i in range(l[0][0], 0, -1):
    lt = []
    for elem in l:
        if i == elem[0]:
            lt.append(elem[1])
    lt.sort()
    for elem in lt:
        print(elem)