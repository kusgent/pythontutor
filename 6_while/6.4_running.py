# http://pythontutor.ru/lessons/while/problems/running/

x = float(input())
y = float(input())
i = 1
while x + x * 0.1 <= y:
    x += x * 0.1
    i += 1
if x < y:
    i += 1
print(i)