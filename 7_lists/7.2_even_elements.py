# http://pythontutor.ru/lessons/lists/problems/even_elements/

n = input().split()
for i in n:
    if int(i) % 2 == 0:
        print(i)