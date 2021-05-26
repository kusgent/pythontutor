# http://pythontutor.ru/lessons/dicts/problems/occurency_index/

l = input().split()

A = dict(zip(l, [-1 for i in range(len(l))]))

for elem in l:
    A[elem] += 1
    print(A[elem], end=' ')