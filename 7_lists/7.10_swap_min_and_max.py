# http://pythontutor.ru/lessons/lists/problems/swap_min_and_max/

l = [int(i) for i in input().split()]
n, m = l.index(min(l)), l.index(max(l))
l[n], l[m] = l[m], l[n]
print(*l)