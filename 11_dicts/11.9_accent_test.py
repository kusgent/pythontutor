# http://pythontutor.ru/lessons/dicts/problems/accent_test/

n = int(input())
l1 = list()
l2 = list()
for i in range(n):
    st = input()
    l1.append(st)
    l2.append(st.lower())

s = input().split()

q = 0
for el in s:
    z = 0
    if el.lower() not in l2:
        for symb in el:
            if symb.isupper() == True:
                z += 1
        if z != 1:
            q += 1
    else:
        if el not in l1:
            q += 1

print(q)