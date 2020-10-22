# http://pythontutor.ru/lessons/str/problems/delete_every_third_char/

s = input()
r = ''
for i in range(len(s)):
    if i % 3 != 0:
        r += s[i]
print(r)