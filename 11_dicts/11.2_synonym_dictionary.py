# http://pythontutor.ru/lessons/dicts/problems/synonym_dictionary/

n = int(input())
D = dict([input().split() for i in range(n)])
m = input()
for key, val in D.items():
    if m == key:
        print(val)
    elif m == val:
        print(key)