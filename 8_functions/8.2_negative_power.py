# http://pythontutor.ru/lessons/functions/problems/negative_power/

def power(a, n):
    p = 1
    if n < 0:
        a = 1 / a
        n = abs(n)
    for i in range(n):
        p *= a
    return p

a = float(input())
n = int(input())
print(power(a, n))