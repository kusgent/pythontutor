# http://pythontutor.ru/lessons/while/problems/seq_avg/

n = int(input())
s = 0
i = 0
while n != 0:
    s += n
    i += 1
    n = int(input())
print(s/i)