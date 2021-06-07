# http://pythontutor.ru/lessons/dicts/problems/countries_and_cities/

n = int(input())
d = {}
for i in range(n):
    l = input().split()
    for j in (range(1, len(l))):
        d[l[j]] = l[0]
m = int(input())
for i in range(m):
    s = input()
    print(d[s])