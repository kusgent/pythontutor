# http://pythontutor.ru/lessons/ifelse/problems/chess_board/

n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())

if (n1+n2)%2==0 and (n3+n4)%2==0:
    print("YES")
elif (n1+n2)%2==1 and (n3+n4)%2==1:
    print("YES")
else:
    print("NO")