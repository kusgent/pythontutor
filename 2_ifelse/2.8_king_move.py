# http://pythontutor.ru/lessons/ifelse/problems/king_move/

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if (n3 == n1 or n3 == n1+1 or n3 == n1-1) and (n4 == n2 or n4 == n2-1 or n4 == n2+1):
    print("YES")
else:
    print("NO")