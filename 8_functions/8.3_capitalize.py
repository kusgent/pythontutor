# http://pythontutor.ru/lessons/functions/problems/capitalize/

def capitalize(s):
    q = s[0].upper()
    r = s[1:]
    s = q + r
    return(s)

l = input().split()
for i in range(len(l)):
    l[i] = capitalize(l[i])
print(*l)