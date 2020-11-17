# http://pythontutor.ru/lessons/lists/problems/even_indices/

l = [i for i in input().split()]
for i in range(len(l)):
    if i % 2 == 0:
        print(l[i])