# http://pythontutor.ru/lessons/lists/problems/lists_queens/

l = [[int(i) for i in input().split()] for i in range(8)]
res = 'NO'
for i in range(7):
    for j in range(i + 1, 7):
        if abs(l[i][0] - l[j][0]) == abs(l[i][1] - l[j][1]) or l[i][0] == l[j][0] or l[i][1] == l[j][1]:
            res = 'YES'
            break
print(res)