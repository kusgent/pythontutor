# http://pythontutor.ru/lessons/while/problems/seq_index_of_max/

n = int(input())
m = 0
i = -1
while n != 0:
    i += 1
    if n > m:
        m = n
        r = i
    n = int(input())
print(r)