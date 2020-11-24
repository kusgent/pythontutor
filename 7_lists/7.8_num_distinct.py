# http://pythontutor.ru/lessons/lists/problems/num_distinct/

l = [int(i) for i in input().split()]
s = []
for i in l:
    if i not in s:
        s.append(i)
print(len(s))