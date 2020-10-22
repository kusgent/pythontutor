# http://pythontutor.ru/lessons/str/problems/delete_chunk/

s = input()
n1 = s.find('h')
n2 = s.rfind('h')
print(s[:n1] + s[n2 + 1:])