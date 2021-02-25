# http://pythontutor.ru/lessons/sets/problems/sets_intersection/

print(*sorted(set([int(i) for i in input().split()]) & set([int(i) for i in input().split()])))