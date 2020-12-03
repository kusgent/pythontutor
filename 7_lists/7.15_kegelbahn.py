# http://pythontutor.ru/lessons/lists/problems/kegelbahn/

l = [int(i) for i in input().split()]
t = [i for i in range(1, l[0] + 1)]
for i in range(l[1]):
    k = [int(i) for i in input().split()]
    t[k[0]-1:k[1]] = ['.'] * (k[1] - k[0] + 1)
for i in range(len(t)):
    if t[i] != '.':
        t[i] = 'I'
print(''.join(t))