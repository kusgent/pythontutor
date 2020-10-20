# http://pythontutor.ru/lessons/str/problems/swap_two_words/

s = input()
n = s.index(' ')
print(s[n + 1:] + ' ' + s[:n])