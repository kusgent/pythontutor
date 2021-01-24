# http://pythontutor.ru/lessons/2d_arrays/problems/diagonals/

n = int(input())
l = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            l[i][j] = j - i
        elif i > j:
            l[i][j] = i - j
for row in l:
    print(*row)