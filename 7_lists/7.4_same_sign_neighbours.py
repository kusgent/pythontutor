# http://pythontutor.ru/lessons/lists/problems/same_sign_neighbours/

l = input().split()
for i in range(1, len(l)):
    if (int(l[i]) > 0 and int(l[i - 1]) > 0) or (int(l[i]) < 0 and int(l[i - 1]) < 0):
        print(l[i - 1], l[i])
        break