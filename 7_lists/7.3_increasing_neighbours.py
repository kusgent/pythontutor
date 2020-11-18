# http://pythontutor.ru/lessons/lists/problems/increasing_neighbours/

l = input().split()
for i in range(1, len(l)):
    if int(l[i]) > int(l[i-1]):
        print(l[i])