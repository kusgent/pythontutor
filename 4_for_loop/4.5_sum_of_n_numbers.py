# http://pythontutor.ru/lessons/for_loop/problems/sum_of_n_numbers/

n = int(input())
s = 0
for i in range(n):
    s += int(input())
print(s)