# http://pythontutor.ru/lessons/sets/problems/guess_number_2/

n = int(input())
all_values = set(range(1, n + 1))  # все значения
likely_values = all_values  # вероятные значения
while True:
    s = input()
    if s == 'HELP':
        break
    l = {int(i) for i in s.split()}
    if len(l) <= len(likely_values) / 2:
        print('NO')
        likely_values -= l
    elif len(l) > len(likely_values) / 2:
        print('YES')
        likely_values &= l

print(*sorted(likely_values))