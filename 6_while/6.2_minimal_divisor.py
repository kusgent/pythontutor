# http://pythontutor.ru/lessons/while/problems/minimal_divisor/

n = int(input())
i = 2
while i <= n:
    if n % i == 0:
        print(i)
        break
    else:
        i += 1