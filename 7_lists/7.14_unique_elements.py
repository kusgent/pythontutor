# http://pythontutor.ru/lessons/lists/problems/unique_elements/

l = input().split()
for i in l:
    if l.count(i) == 1:
        print(i)