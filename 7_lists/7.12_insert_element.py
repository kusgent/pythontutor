# http://pythontutor.ru/lessons/lists/problems/insert_element/

l = [int(i) for i in input().split()]
x = input().split()
k, c = int(x[0]), int(x[1])
for i in range(k, len(l)):
    a = l[i]
    l[i] = c
    c = a
l.append(c)
print(*l)