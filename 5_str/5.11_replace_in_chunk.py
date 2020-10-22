# http://pythontutor.ru/lessons/str/problems/replace_in_chunk/

s = input()
n1 = s.find('h')
n2 = s.rfind('h')
print(s[:n1 + 1] + s[n1 + 1:n2].replace('h', 'H') + s[n2:])