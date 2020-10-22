# http://pythontutor.ru/lessons/str/problems/reverse_chunk/

s = input()
n1 = s.find('h')
n2 = s.rfind('h')
#print(s[n2 - 1:n1:-1])
print(s[:n1 + 1] + s[n2 - 1:n1:-1] + s[n2:])