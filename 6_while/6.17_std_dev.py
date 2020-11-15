# http://pythontutor.ru/lessons/while/problems/std_dev/

n = int(input())
r = s = 0
p = []
while n != 0:
    s += n
    r += 1
    p.append(n)
    n = int(input())
h = 0
for i in range(len(p)):
    h += (p[i] - (s/r))**2
print((h/(r - 1))**0.5)