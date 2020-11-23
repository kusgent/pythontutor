# http://pythontutor.ru/lessons/lists/problems/lineup/

l = [int(i) for i in input().split()]
x = int(input())
n = 0
for i in l:
    if i >= x:
        n += 1
print(n + 1)