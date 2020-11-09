# http://pythontutor.ru/lessons/while/problems/seq_num_maximal/

n = int(input())
m = 0
while n != 0:
    if n > m:
        m, q = n, 1
    elif n == m:
        q += 1
    n = int(input())
print(q)