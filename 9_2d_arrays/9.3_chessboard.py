# http://pythontutor.ru/lessons/2d_arrays/problems/chessboard/

n, m = [int(i) for i in input().split()]
l = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if abs(i - j) % 2 == 1:
            l[i][j] = '*'
for row in l:
    print(*row)