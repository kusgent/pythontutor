# http://pythontutor.ru/lessons/dicts/problems/genealogy_lca/

n = int(input())
d = dict()  # начальный словарь с входными данными
for i in range(n - 1):
    l = input().split()
    d[l[0]] = l[1]

keys_set = set(d.keys())
values_set = set(d.values())
parent = list(values_set - keys_set)[0]

result_dict = {parent: 0}  # итоговый словарь со значениями глубины по каждому элементу
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


# функция для определения общего предка у двух элементов с равной глубиной
def com_anc(a, b):
    while a != b:
        a = d[a]
        b = d[b]
    return a


n = int(input())
for i in range(n):
    l = input().split()
    if result_dict[l[0]] == result_dict[l[1]]:
        print(com_anc(l[0], l[1]))
    elif result_dict[l[0]] < result_dict[l[1]]:
        q = result_dict[l[1]]  # фиксируем глубину начального потомка
        child = l[1]  # фиксируем начального потомка
        while q > result_dict[l[0]]:
            child = d[child]
            q -= 1
        if child == l[0]:  # первый явл. предком второго и общим предком для обоих
            print(l[0])
        else:  # у элементов есть общий третий предок
            print(com_anc(l[0], child))
    else:
        q = result_dict[l[0]]  # фиксируем глубину начального потомка
        child = l[0]  # фиксируем начального потомка
        while q > result_dict[l[1]]:
            child = d[child]
            q -= 1
        if child == l[1]:  # второй явл. предком первого и общим предком для обоих
            print(l[1])
        else:  # у элементов есть общий третий предок
            print(com_anc(child, l[1]))
