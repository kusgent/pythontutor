# http://pythontutor.ru/lessons/ifelse/problems/queen_move/

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if abs(n1-n3)==abs(n2-n4) or (n1 == n3 or n2 == n4):
    print("YES")
else:
    print("NO")