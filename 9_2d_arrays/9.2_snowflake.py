# http://pythontutor.ru/lessons/2d_arrays/problems/snowflake/

n = int(input())
l = [['.'] * n for i in range(n)]
for i in range(n):
    l[i][i] = '*' # main diagonal
    l[n // 2][i] = '*' # middle line
    l[i][n // 2] = '*' # middle column
    l[i][(n - 1) - i] = '*' # side diagonal
for row in l:
    print(' '.join(row))