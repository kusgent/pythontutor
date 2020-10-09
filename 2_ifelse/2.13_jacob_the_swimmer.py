# http://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/

N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N >= M:
    if N - y <= y:
        y = N - y
    if M - x <= x:
        x = M - x
    if x >= y:
        print(y)
    else:
        print(x)
elif N < M:
    if M - y <= y:
        y = M - y
    if N - x <= x:
        x = N - x
    if x >= y:
        print(y)
    else:
        print(x)