# http://pythontutor.ru/lessons/while/problems/powers_of_two/

n = int(input())
i = 0
r = 1
while r * 2 <= n:
    r *= 2
    i += 1
print(i, r)