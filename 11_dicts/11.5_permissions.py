# http://pythontutor.ru/lessons/dicts/problems/permissions/

n = int(input())
d = dict([(input().split(' ', 1)) for i in range(n)])

for elem in d:
    l = []
    for i in d[elem].split():
        if i == 'W':
            l.append('write')
        elif i == 'R':
            l.append('read')
        elif i == 'X':
            l.append('execute')
        d[elem] = l

m = int(input())
for i in range(m):
    l = input().split()
    if l[1] in d and l[0] in d[l[1]]:
        print('OK')
    else:
        print('Access denied')