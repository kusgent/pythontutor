# http://pythontutor.ru/lessons/ifelse/problems/knight_move/

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if (abs(n3 - n1) == 1 and abs(n4 - n2) == 2) or (abs(n3 - n1) == 2 and abs(n4 - n2) == 1):
    print("YES")
else:
    print("NO")