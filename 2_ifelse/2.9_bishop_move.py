# http://pythontutor.ru/lessons/ifelse/problems/bishop_move/

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if abs(n1-n3)==abs(n2-n4):
    print("YES")
else:
    print("NO")