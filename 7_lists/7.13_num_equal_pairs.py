# http://pythontutor.ru/lessons/lists/problems/num_equal_pairs/

l = input().split()
q = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            q += 1
print(q)