# http://pythontutor.ru/lessons/lists/problems/remove_element/

l = [int(i) for i in input().split()]
k = int(input())
for i in range(k, len(l) - 1):
    l[i] = l[i + 1]
l.pop()
print(*l)