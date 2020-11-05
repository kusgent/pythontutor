# http://pythontutor.ru/lessons/while/problems/seq_increasing_neighbours/

n = int(input())
i = 0
while n != 0:
    m = int(input())
    if m > n:
        i += 1
    n = m
print(i)