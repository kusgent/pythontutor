# http://pythontutor.ru/lessons/2d_arrays/problems/swap_columns/

def swap_columns(l, a, b):
    for i in range(len(l)):
        l[i][a], l[i][b] = l[i][b], l[i][a]
    for row in l:
        print(*row)

n, m = [int(i) for i in input().split()]
l = [[int(j) for j in input().split()] for i in range(n)]
a, b = [int(i) for i in input().split()]
swap_columns(l, a, b)