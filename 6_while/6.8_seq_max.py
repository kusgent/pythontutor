# http://pythontutor.ru/lessons/while/problems/seq_max/

n = int(input())
i = 0
while n != 0:
    if n > i:
        i = n
    n = int(input())
print(i)