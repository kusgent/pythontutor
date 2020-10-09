# http://pythontutor.ru/lessons/int_and_float/problems/konec_urokov/

n = int(input())

n1 = n // 2
n2 = n - n1 - 1
V = n * 45 + n1 * 5 + n2 * 15

print(V // 60 + 9, V % 60)