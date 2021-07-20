# http://pythontutor.ru/lessons/dicts/problems/accent_test/

n = int(input())
l = list()
for i in range(n):
    l.append(input())

s = input().split()

q = 0
for el in s:
    z = 0
    if el not in l:
        for symb in el:
            if symb.isupper() == True:
                z += 1
        if z != 1:
            q += 1

print(q)