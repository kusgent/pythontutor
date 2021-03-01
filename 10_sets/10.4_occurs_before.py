# http://pythontutor.ru/lessons/sets/problems/occurs_before/

l = input().split()
s = set()
q = len(s)
for i in l:
    s.add(i)
    if len(s) > q:
        q = len(s)
        print('NO')
    else:
        print('YES')