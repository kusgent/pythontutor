# http://pythontutor.ru/lessons/dicts/problems/usa_elections/

n = int(input())
l = sorted([input().split() for i in range(n)])
d = {}

for i in l:
    d[i[0]] = d.get(i[0], 0) + int(i[1])

for key in d:
    print(key, d[key])