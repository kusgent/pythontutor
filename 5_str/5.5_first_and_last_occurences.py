# http://pythontutor.ru/lessons/str/problems/first_and_last_occurences/

s = input()
q = s.count('f')
if q == 1:
    print(s.index('f'))
elif q >= 2:
    print(s.find('f'), s.rfind('f'))