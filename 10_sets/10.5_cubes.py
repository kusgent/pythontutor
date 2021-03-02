# http://pythontutor.ru/lessons/sets/problems/cubes/

l = [int(i) for i in input().split()]
s1, s2 = set(), set()
for i in range(l[0]):
    s1.add(int(input()))
for i in range(l[1]):
    s2.add(int(input()))

print(len(s1 & s2))
print(*sorted(s1 & s2))

print(len(s1 - s2))
print(*sorted(s1 - s2))

print(len(s2 - s1))
print(*sorted(s2 - s1))