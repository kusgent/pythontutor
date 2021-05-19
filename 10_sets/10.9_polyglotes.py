# http://pythontutor.ru/lessons/sets/problems/polyglotes/

n = int(input())
s1, s2 = set(), set()
for i in range(n):
    q = int(input())
    overall_set = set()
    for j in range(q):
        overall_set.add(input())
    if len(s1) == 0:
        s1 = overall_set
    s1 &= overall_set
    s2 |= overall_set
result = [s1, s2]
for elem in result:
    print(len(elem))
    s = sorted(elem)
    for elem in s:
        print(elem)