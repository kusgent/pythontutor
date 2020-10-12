# http://pythontutor.ru/lessons/for_loop/problems/lost_card/

n = int(input())
f1 = 1
f2 = 1
for i in range(1, n + 1):
    f1 *= i
for i in range(1, n):
    f2 *= int(input())
print(int(f1/f2))