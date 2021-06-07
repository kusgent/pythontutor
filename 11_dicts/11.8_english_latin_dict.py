# http://pythontutor.ru/lessons/dicts/problems/english_latin_dict/

n = int(input())
d = {}
for i in range(n):
    l = input().split(' - ')
    d[l[0]] = l[1]
r = {}
for key, val in d.items():
    for elem in val.split(', '):
        r[elem] = r.get(elem, []) + [key]
for elem in r:
    r[elem].sort()
k = sorted(r)
print(len(k))
for elem in k:
    print(elem + ' - ' + ', '.join(r[elem]))