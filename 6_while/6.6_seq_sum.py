# http://pythontutor.ru/lessons/while/problems/seq_sum/

n = int(input())
s = n
while n != 0:
    n = int(input())
    s += n
print(s)