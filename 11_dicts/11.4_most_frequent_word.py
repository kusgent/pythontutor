# http://pythontutor.ru/lessons/dicts/problems/most_frequent_word/

q = int(input())
d = {}
for i in range(q):
    l = input().split()
    for elem in l:
        d[elem] = d.get(elem, 0) + 1
r = []
for elem in d:
    if d[elem] == max(d.values()):
        r.append(elem)
r.sort()
print(r[0])