# http://pythontutor.ru/lessons/dicts/problems/sales/

d = dict()
while True:
    try:
        temp_list = input().rsplit(' ', 1)
    except:
        break
    d[temp_list[0]] = d.get(temp_list[0], 0) + int(temp_list[1])

r = dict()
for key in d:
    l = key.split()
    if l[0] not in r:
        r[l[0]] = {l[1]: d[key]}
    else:
        r[l[0]][l[1]] = d[key]

l1 = list(r.keys())
l1.sort()

for i in l1:
    l2 = list(r[i].keys())
    l2.sort()
    print(i + ':')
    for j in l2:
        print(j, r[i][j])
