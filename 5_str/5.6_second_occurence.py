# http://pythontutor.ru/lessons/str/problems/second_occurence/

s = input()
q = s.count('f')
if q >= 2:
    print(s.find('f', s.find('f') + 1))
elif q == 1:
    print(-1)
else:
    print(-2)