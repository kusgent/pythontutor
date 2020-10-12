# http://pythontutor.ru/lessons/for_loop/problems/sum_of_factorials/

n = int(input())
m = 1
sm = 0
for i in range(1, n + 1):
    m *= i
    sm += m
print(sm)