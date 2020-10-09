# http://pythontutor.ru/lessons/ifelse/problems/rook_move/

n1 = int(input("Число от 1 до 8 №1: "))
n2 = int(input("Число от 1 до 8 №2: "))
n3 = int(input("Число от 1 до 8 №3: "))
n4 = int(input("Число от 1 до 8 №4: "))

if n1 == n3 or n2 == n4:
    print("YES")
else:
    print("NO")