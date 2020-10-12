# http://pythontutor.ru/lessons/for_loop/problems/factorial/

n = int(input())
m = 1
for i in range(1, n + 1):
    m *= i
print(m)