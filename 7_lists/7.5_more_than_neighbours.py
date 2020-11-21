# http://pythontutor.ru/lessons/lists/problems/more_than_neighbours/

l = [int(i) for i in input().split()]
q = 0
for i in range(1, len(l) - 1):
    if l[i - 1] < l[i] > l[i + 1]:
        q += 1
print(q)