# http://pythontutor.ru/lessons/dicts/problems/genealogy_ancestors_and_descendants/

n = int(input())
d = dict()
for i in range(n - 1):
    l = input().split()
    d[l[0]] = l[1]

keys_set = set(d.keys())
values_set = set(d.values())
parent = list(values_set - keys_set)[0]

result_dict = {parent: 0}
q = len(d)
parents_list = [parent]
while q != 0:
    parents_list_new = list()
    for i in parents_list:
        for key, value in d.items():
            if value == i:
                result_dict[key] = result_dict[i] + 1
                parents_list_new.append(key)
                q -= 1
    parents_list = parents_list_new

n = int(input())
for i in range(n):
    l = input().split()
    if result_dict[l[0]] == result_dict[l[1]]:
        print(0, end=' ')
    elif result_dict[l[0]] < result_dict[l[1]]:
        q = result_dict[l[1]]
        child = l[1]  # фиксируем начального потомка
        while q > result_dict[l[0]]:
            child = d[child]
            q -= 1
        if child == l[0]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    else:
        q = result_dict[l[0]]
        child = l[0]  # фиксируем начального потомка
        while q > result_dict[l[1]]:
            child = d[child]
            q -= 1
        if child == l[1]:
            print(2, end=' ')
        else:
            print(0, end=' ')
