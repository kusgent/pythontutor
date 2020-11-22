# http://pythontutor.ru/lessons/lists/problems/maximal_element/

l = [int(i) for i in input().split()]
s, j = l[0], 0
for i in range(1, len(l)):
    if l[i] > s:
        s, j = l[i], i
print(s, j)