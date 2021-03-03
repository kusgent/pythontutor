# http://pythontutor.ru/lessons/sets/problems/guess_number/

def check_set():
    s = input()
    if s != 'HELP':
        s = set([int(i) for i in s.split()])
    return(s)

n = int(input())
s1 = set([int(i) for i in range(1, n + 1)])
s2 = check_set()
while s2 != 'HELP':
    a = input()
    if a == 'YES':
        s1 &= s2
    elif a == 'NO':
        s1 -= s2
    s2 = check_set()
print(*s1)