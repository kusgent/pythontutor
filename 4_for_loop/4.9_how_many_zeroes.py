# http://pythontutor.ru/lessons/for_loop/problems/how_many_zeroes/

n = int(input())
q = 0
for i in range(n):
    if int(input()) == 0:
        q += 1
print(q)