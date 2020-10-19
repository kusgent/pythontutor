# http://pythontutor.ru/lessons/str/problems/two_halves/

s = input()
l1 = int(len(s)/2)
l2 = len(s[l1:]) - l1
print(s[l1 + l2:] + s[:l1 + l2])