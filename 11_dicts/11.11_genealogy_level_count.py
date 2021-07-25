# http://pythontutor.ru/lessons/dicts/problems/genealogy_level_count/

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

l = list(result_dict.keys())
l.sort()
for key in l:
    print(key, result_dict[key])
