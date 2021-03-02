# http://pythontutor.ru/lessons/sets/problems/number_of_words/

q = int(input())
l = []
for i in range(q):
    l += input().split()

s = set(l)
print(len(s))