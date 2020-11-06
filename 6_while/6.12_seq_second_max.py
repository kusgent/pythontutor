# http://pythontutor.ru/lessons/while/problems/seq_second_max/

t = int(input())
m = 0
p_m = 0
while t != 0:
    if t > m:
        p_m, m = m, t
    elif t > p_m:
        p_m = t
    t = int(input())
print(p_m)