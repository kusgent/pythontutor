# http://pythontutor.ru/lessons/2d_arrays/problems/secondary_diagonal/

n = int(input())
l = [[0] * ((n - 1) - i) + [1] + [2] * i for i in range(n)]
for row in l:
    print(*row)